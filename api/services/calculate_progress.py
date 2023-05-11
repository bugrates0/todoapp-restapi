from api.databases.database import tasks

#Function for calculating progress of to-do list
def calculate_progress(liste: list):
    is_done = 0
    all_tasks = 0
    for task in tasks:
        if liste['id'] == task['listID']:
            if task['removedAt'] == None:
                all_tasks = all_tasks + 1
                if task['isDone'] == True:
                    is_done = is_done + 1
                        
    progress = (is_done*100) /all_tasks
    return int(progress)