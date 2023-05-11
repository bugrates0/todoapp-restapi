from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import create_access_token
from api.databases.database import users



class Login(Resource):
    
    def post(self):
        username = request.json.get("username", None)
        password = request.json.get("password", None)
        if not any(username == user['username'] and password == user['password'] for user in users ):
            return jsonify({"message": "Wrong username or password"}), 401
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token) 