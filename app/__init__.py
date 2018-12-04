from flask import Flask
from flask_restful import Api , Resource

#local import
from .api.v1.redflags.views import RedFlag, ManageRedFlag, RedFlagDelete

def create_app():
    app = Flask(__name__)
    api = Api(app)


    api.add_resource(RedFlag, '/api/v1/redflags')
    api.add_resource(RedFlagDelete, '/api/v1/redflags/<int:id>')
    api.add_resource(ManageRedFlag, '/api/v1/redflag/<int:id>')
    return app 