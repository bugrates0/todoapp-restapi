from app import app
from datetime import datetime
from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from api.databases.database import tasks, todo_lists
from api.services.calculate_progress import calculate_progress

#################################################################################################
#   Requests for tasks (accesible for all kind of users)
                

class Tasks_Get_Put(Resource):
    
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        my_tasks = []
        for task in tasks:
            if task['listID'] == current_user and task['removedAt'] == None:
                my_tasks.append(task)
        if my_tasks == []:
            return jsonify({"Message": "You don't have any tasks."})
        else:
            return my_tasks
                        
        
    
    @jwt_required()
    def post(self):
        current_user = get_jwt_identity()
        if bool(todo_lists) is True:
            if not any(liste['id'] == current_user and liste['removedAt'] == None for liste in todo_lists):
                return jsonify({"Message": "You should create a to-do list before creating a task !"})    
            for liste in todo_lists:
                if liste['id'] == current_user and liste['removedAt'] == None:
                    data = request.json
                    task_id = sum(task['listID'] == current_user for task in tasks) + 1
                    creation_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    new_task = {'id': task_id, 'listID': current_user, 'createdAt': creation_time, 'updatedAt': None, 'removedAt': None, 'task': data['task'], 'isDone': False }
                    tasks.append(new_task)
                    liste['updatedAt'] = creation_time
                    liste['progress'] = "%" + str (calculate_progress(liste))
                    return new_task
        else:
            return jsonify({"Message": "You should create a to-do list before creating a task !"})      
                          
                


    
@app.route("/todoapp/api/tasks/<task_id>", methods=["DELETE"])        
@jwt_required()
def delete(task_id):
    current_user = get_jwt_identity()
    for task in tasks:
        if task['listID'] == current_user:
            if task['removedAt'] == None:
                if task ['id'] == int(task_id):
                    remove_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    task['removedAt'] = remove_time
                    for liste in todo_lists:
                        if liste['id'] == task['listID'] and liste['removedAt'] == None:
                            liste['updatedAt'] = remove_time
                            liste['progress'] = "%" + str (calculate_progress(liste))
                    return jsonify({"Message":"Task has been deleted !"})
                    


@app.route("/todoapp/api/tasks/<task_id>/task", methods=["PUT"])
@jwt_required()
def update_task(task_id):
        current_user = get_jwt_identity()
        if bool(tasks) is True:               
            for task in tasks:
                if task['listID'] == current_user:
                    if task['removedAt'] == None:
                        if task ['id'] == int(task_id):
                            data = request.json
                            update_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            task['updatedAt'] = update_time
                            task['task'] = data['task']
                            for liste in todo_lists:
                                if liste['id'] == task['listID'] and liste['removedAt'] == None:
                                    liste['updatedAt'] = update_time
                            return task
        else:
            return jsonify({"Message": "You don't have any task !"})


@app.route("/todoapp/api/tasks/<task_id>/isdone", methods=["PUT"])
@jwt_required()
def update_task_status(task_id):
    current_user = get_jwt_identity()
    if bool(tasks) is True:
        for task in tasks:
            if task['listID'] == current_user:
                if task['removedAt'] == None:
                    if task ['id'] == int(task_id):
                        data = request.json
                        update_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        task['updatedAt'] = update_time
                        task['isDone'] = data['isDone']
                        for liste in todo_lists:
                            if liste['id'] == task['listID'] and liste['removedAt'] == None:
                                liste['updatedAt'] = update_time
                                liste['progress'] = "%" + str (calculate_progress(liste))
                        return task
    else:
        return jsonify({"Message": "You don't have any task !"})
