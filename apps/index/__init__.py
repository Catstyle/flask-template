from flask import Blueprint
from flask_restful import Api


bp = Blueprint('index', __name__)
api = Api(bp)


from . import urls  # noqa
