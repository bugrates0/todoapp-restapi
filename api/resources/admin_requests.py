from flask import jsonify
from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from api.databases.database import tasks, todo_lists,users


#################################################################################################
#   Only Admin Requests

class Admin_Get_Lists(Resource):
    
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        for user in users:
            if user['username'] == current_user and user['isAdmin'] == True:
                if bool(todo_lists):
                    return jsonify(todo_lists)
                else:
                    return jsonify({"Message": "No to-do lists !"})
      
      
class Admin_Get_Tasks(Resource):
    
    @jwt_required()
    def get(self, user_name):
        current_user = get_jwt_identity()
        user_tasks = []
        for user in users:
            if user['username'] == current_user and user['isAdmin'] == True:
                if bool(tasks):
                    if not any(user['username'] == user_name for user in users):
                        return jsonify({"Message":"Please try for valid user"})
                    for task in tasks:
                        if task['listID'] == user_name:
                            user_tasks.append(task)
                    return jsonify(user_tasks)
                else:
                    if not any(user['username'] == user_name for user in users):
                        return jsonify({"Message":"Please try for valid user"})
                    return jsonify({"Message": "No tasks !"})

#################################################################################################     