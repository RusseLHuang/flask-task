from flask_restful import Resource
from src.task.task_entity import Task
from src.db import get_db, get_db_session

class TasksController(Resource):
  def get(self):
    Session = get_db_session()
    session = Session()

    task_list = []
    for u in session.query(Task).all():
      task_list.append(dict(u))

    return { "result": task_list }, 200, {'content-type': 'application/json'}
