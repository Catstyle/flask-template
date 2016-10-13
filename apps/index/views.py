# -*- coding: utf-8 -*-

from flask import render_template
from flask_restful import Resource
from flask_login import login_required


class IndexView(Resource):

    @login_required
    def get(self, *args, **kwargs):
        return render_template('modules/core/frame.tpl.html')


class SigninView(Resource):

    def get(self, *args, **kwargs):
        return render_template('modules/core/frame.tpl.html')
