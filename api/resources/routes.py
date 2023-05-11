from api.resources.todolists import Todo_Lists
from api.resources.tasks import Tasks_Get_Put
from api.resources.auth import Login
from api.resources.admin_requests import Admin_Get_Lists, Admin_Get_Tasks

def init_routes(api):
    api.add_resource(Tasks_Get_Put, '/todoapp/api/tasks')
    api.add_resource(Todo_Lists, '/todoapp/api/todolist')
    api.add_resource(Login, '/login')
    api.add_resource(Admin_Get_Lists, '/todoapp/api/todolists')
    api.add_resource(Admin_Get_Tasks, '/todoapp/api/tasks/<user_name>')
