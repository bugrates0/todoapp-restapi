from datetime import datetime
from api.databases.database import tasks, todo_lists
from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required



#################################################################################################
#   Requests for todo lists (accesible for all kind of users)


class Todo_Lists(Resource):

    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        if bool(todo_lists) is True:
            if not any(liste['id'] == current_user for liste in todo_lists):
                return jsonify({"Message": "You don't have a to-do list, please create a new one !"})
            if not any(liste['id'] == current_user and liste['removedAt'] == None for liste in todo_lists): 
                return jsonify({"Message": "You don't have a to-do list, please create a new one !"})
            for liste in todo_lists:
                if liste['id'] == current_user and liste['removedAt'] ==None:
                    return liste
        else:
            return jsonify({"Message": "You don't have a to-do list, please create a new one !"})
            
            
            
    # According to the instructions, a user will only have one to-do list.   
    @jwt_required()
    def post(self):
        current_user = get_jwt_identity()
        if bool(todo_lists) is False:
            data = request.json
            creation_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            new_list = {'id': current_user, 'name': data['name'], 'createdAt': creation_time, 'updatedAt': None, 'removedAt': None, 'progress': None}
            todo_lists.append(new_list)
            return new_list
        else:
            if not any(liste['id'] == current_user for liste in todo_lists):
                data = request.json
                creation_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                new_list = {'id': current_user, 'name': data['name'], 'createdAt': creation_time, 'updatedAt': None, 'removedAt': None, 'progress': None}
                todo_lists.append(new_list)
                return new_list 
            if any(liste['id'] == current_user and liste['removedAt'] == None for liste in todo_lists):
                return jsonify({'message': "You have already a to-do list !"})
            if not any(liste['id'] == current_user and liste['removedAt'] == None for liste in todo_lists):
                data = request.json
                creation_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                new_list = {'id': current_user, 'name': data['name'], 'createdAt': creation_time, 'updatedAt': None, 'removedAt': None, 'progress': None}
                todo_lists.append(new_list)
                return new_list

 

    @jwt_required()
    def delete(self):  
        current_user = get_jwt_identity()
        if bool(todo_lists) is True:
            if not any(liste['id'] == current_user and liste['removedAt'] == None for liste in todo_lists):
                return jsonify({"Message": "You don't have a to-do list, please create a new one !"})
            for liste in todo_lists:
                if liste['id'] == current_user:
                    if liste['removedAt'] == None:
                        remove_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        liste['removedAt'] = remove_time
                        for task in tasks:
                            if task['listID'] == liste['id']:
                                task['removedAt'] = remove_time
                        return jsonify({"Message": "List has been deleted successfully !"})
        else:
            return jsonify({"Message": "You don't have a to-do list, please create a new one !"})
        
        
                

        