from . import api
from . import restful


api.add_resource(restful.Login, '/login/')
api.add_resource(restful.Logout, '/logout/')
