from . import api
from .views import IndexView, SigninView


api.add_resource(IndexView, '/')
api.add_resource(SigninView, '/signin')
