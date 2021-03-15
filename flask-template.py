#!/usr/bin/env python
import os
import secrets
import shutil

from argparse import ArgumentParser
from subprocess import check_call, call


def parse_args():
    parser = ArgumentParser()
    parser.add_argument(
        'name', type=str,
        help='project name, this name will replace placeholder in config files'
    )

    args = parser.parse_args()

    print('args:', args)
    return args


def confirm(prompt):
    return input(prompt + ' (y/n): ').lower() in ('y', 'yes')


def clone_template(pathname):
    if os.path.exists(pathname):
        if confirm('%s already exists, do you want to overwrite it? '
                   '(yes will delete it first)' % pathname):
            print('deleting %s...' % pathname)
            shutil.rmtree(pathname)
        else:
            print('giveup git clone')
            exit(1)
    check_call(['cp', '-r', '.', pathname])


def replace_placeholder(name, length=32):
    print()
    print('replacing placeholder to %s in config files...' % name)
    secret = secrets.base64.b64encode(secrets.token_bytes(length))
    secret = secret.decode('utf-8').replace('/', '')
    check_call(
        ["sed -i s/--secret-key--/%s/g core/conf/default.py" % secret],
        shell=True,
    )


def initiate(name):
    print()
    print('initiating virtual env...')
    check_call(['virtualenv', 'venv'])
    check_call(
        ['. venv/bin/activate && pip install -U pip && '
         'pip install -i https://pypi.doubanio.com/simple '
         '-r requirements.txt'],
        shell=True
    )
    check_call(
        ['. venv/bin/activate && pip install -U pip && '
         'pip install -i https://pypi.doubanio.com/simple '
         '-r requirements-dev.txt'],
        shell=True
    )

    print()
    print('reset git...')
    check_call(['rm', '.git', '-rf'])
    check_call(['git', 'init'])
    check_call(['git', 'add', '.'])

    print()
    print('committing...')
    check_call(
        ['. venv/bin/activate && pre-commit install && '
         'git commit -am "initialized %s from template"' % name.strip('../')],
        shell=True,
    )

    print('making dirs... logs')
    call(['mkdir', '-p', 'logs'])


def main():
    args = parse_args()
    name = args.name
    clone_template(name)
    os.chdir(name)
    replace_placeholder(name)
    initiate(name)


if __name__ == '__main__':
    main()
