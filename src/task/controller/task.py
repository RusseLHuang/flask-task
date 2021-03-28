from flask_restful import Resource, reqparse
from src.task.task_entity import Task
from src.db import get_db, get_db_session

task_post_parser = reqparse.RequestParser()
task_post_parser.add_argument("name", type=str, required=True)

class TaskController(Resource):
  def post(self):
    args = task_post_parser.parse_args()

    Session = get_db_session()
    session = Session()
    new_task = Task(args['name'], False)

    session.add(new_task)
    session.commit()

    return { "result": dict(new_task) }, 201, {'content-type': 'application/json'}
