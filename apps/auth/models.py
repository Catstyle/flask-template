# coding=utf-8
from time import time

import flask_bcrypt
from flask_login import UserMixin

from core.ext import db


class UserProfile(UserMixin, db.Document):
    # 用户表

    username = db.StringField(required=True)
    password = db.StringField(required=True)
    is_active = db.BooleanField(default=True)
    is_super = db.BooleanField(default=False)
    created_time = db.FloatField(default=time)

    def set_password(self, password):
        """修改密码"""
        self.password = flask_bcrypt.generate_password_hash(password)
        self.save()

    def check_password(self, password):
        """验证密码"""
        return flask_bcrypt.check_password_hash(self.password, password)

    meta = {
        "collection": "user",
        'indexes': [
            {'fields': ['username'], 'unique': True},
        ]
    }
