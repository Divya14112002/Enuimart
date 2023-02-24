import os
from flask import Flask 
from flask_restful import Resource, Api 
from application.config import LocalDevelopmentConfig
from application.database import db 

app,api = None, None

def create_app():
    app = Flask(__name__,template_folder="templates")
    if os.getenv('ENV',"development")=="production" : 
        raise Exception('PRODUCTION SETUP NOT YET READY')
    else:
        print('Starting local Devlopment Environment')
        app.config.from_object(LocalDevelopmentConfig)
    db.init_app(app)
    api = Api(app)
    app.app_context().push()
    return app,api

app,api = create_app()  

from application.api import registration_API
api.add_resource(registration_API,"/api/user")

if __name__ == '_main__':
    app.run(host='0.0.0.0', port=8000)