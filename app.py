from datetime import timedelta
from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager


app = Flask(__name__)
api = Api(app)

app.config["JWT_SECRET_KEY"] = "secretkey" 
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
jwt = JWTManager(app)

from api.resources.routes import init_routes

    
init_routes(api)