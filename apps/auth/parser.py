# coding=utf-8
from flask_restful import reqparse, inputs


username = inputs.regex(r'\w{1,10}')
password = inputs.regex(r'\w{6,24}')

user_parser = reqparse.RequestParser(bundle_errors=True)
user_parser.add_argument('username', type=username, required=True)
user_parser.add_argument('password', type=password, required=True)
