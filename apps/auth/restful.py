# -*- coding: utf-8 -*-
from flask import request
from flask_restful import Resource
from flask_login import login_user, logout_user, login_required

from core import logger
from core.utils import make_response

from . import parser
from .models import UserProfile


@logger.trace_view
@logger.class_logger
class Login(Resource):

    def post(self):
        # 登陆请求
        req = parser.user_parser.parse_args(strict=True)

        user_obj = UserProfile.objects(username=req['username']).first()

        if user_obj and user_obj.check_password(req['password']):
            login_user(user_obj, remember=True)
            return make_response(status=10000)
        else:
            self.logger.warning("{}密码验证失败！".format(request.remote_addr))
            return make_response(status=10001)


@logger.trace_view
@logger.class_logger
class Logout(Resource):

    @login_required
    def get(self):
        logout_user()
        return make_response(status=10000)
