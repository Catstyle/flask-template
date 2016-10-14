#!/usr/bin/env python
from __future__ import print_function

import os
import shutil
from subprocess import check_call, call
from argparse import ArgumentParser


def parse_args():
    parser = ArgumentParser()
    parser.add_argument(
        'name', type=str,
        help='project name, this name will replace placeholder in config files'
    )
    parser.add_argument(
        '--dir', type=str, default='.', help='change output dir'
    )

    args = parser.parse_args()
    args.template_url = 'git@git.cdecube.com:wolong/flask-restful-template.git'

    print('args:', args)
    return args


def confirm(prompt):
    return raw_input(prompt + ' (y/n): ').lower() in ('y', 'yes')  # noqa


def clone_template(url, pathname):
    if os.path.exists(pathname):
        if confirm('%s already exists, do you want to overwrite it? '
                   '(yes will delete it first)' % pathname):
            print('deleting %s...' % pathname)
            shutil.rmtree(pathname)
        else:
            print('giveup git clone')
            exit(1)
    check_call(['git', 'clone', url, pathname])


def replace_placeholder(name):
    print()
    print('replacing placeholder to %s in config files...' % name)
    check_call(
        ["find . -type f | xargs grep name-- | "
         "awk -F: '{print $1}' | xargs sed -i s/--name--/%s/g " % name],
        shell=True
    )


def initiate(name):
    print()
    print('initiating virtual env...')
    check_call(['virtualenv', 'venv'])
    check_call(
        ['. venv/bin/activate && pip install -U pip && '
         'pip install -i http://pypi.doubanio.com/simple '
         '--trusted-host pypi.doubanio.com -r requirements.txt'],
        shell=True
    )

    print()
    print('installing pre-commit...')
    check_call(['. venv/bin/activate && pre-commit install'], shell=True)

    print()
    print('committing...')
    check_call(
        ['git', 'commit', '-am', '"initialized %s from template"' % name]
    )

    print()
    print('try installing git flow...')
    call(['git', 'flow', 'init', '-d'])

    print()
    print('removing git origin remote url...')
    check_call(['git', 'remote', 'remove', 'origin'])

    print('making dirs... logs')
    call(['mkdir', 'logs'])


def main():
    args = parse_args()
    os.chdir(args.dir)
    name = args.name
    clone_template(args.template_url, name)
    os.chdir(name)
    replace_placeholder(name)
    initiate(name)


if __name__ == '__main__':
    main()
