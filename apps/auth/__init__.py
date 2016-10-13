from flask import Blueprint
from flask_restful import Api


bp = Blueprint('auth', __name__)
api = Api(bp)


from . import urls  # noqa
