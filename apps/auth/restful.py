# -*- coding: utf-8 -*-
from flask import request
from flask_restful import Resource
from flask_login import login_user, logout_user, login_required

from core import logger

from . import parser
from .models import UserProfile


@logger.trace_view
@logger.class_logger
class Login(Resource):

    def post(self):
        req = parser.user_parser.parse_args(strict=True)
        user_obj = UserProfile.objects(username=req['username']).first()

        if user_obj and user_obj.check_password(req['password']):
            login_user(user_obj)
            return ''
        else:
            self.logger.warning("{}密码验证失败！".format(request.remote_addr))
            return '', 401


@logger.trace_view
@logger.class_logger
class Logout(Resource):

    @login_required
    def get(self):
        logout_user()
        return ''
