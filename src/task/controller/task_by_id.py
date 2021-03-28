from sqlalchemy.dialects.mysql import insert
from flask_restful import Resource, reqparse
from src.task.task_entity import Task
from src.db import get_db, get_db_session

task_put_parser = reqparse.RequestParser()
task_put_parser.add_argument("id", type=int, required=True)
task_put_parser.add_argument("name", type=str, required=True)
task_put_parser.add_argument("status", type=bool, required=True)

class TaskByIdController(Resource):
  def put(self, task_id):
    args = task_put_parser.parse_args()

    if task_id is not args['id']:
      return {}, 500

    insert_statement = insert(Task).values(
      id=task_id,
      name=args['name'],
      status=args['status'],
    )

    on_duplicated_statement = insert_statement.on_duplicate_key_update(
      name=args['name'],
      status=args['status'],
    )

    with get_db().connect() as connection:
      connection.execute(on_duplicated_statement)

    return args

  def delete(self, task_id):
    Session = get_db_session()
    session = Session()

    delete_result = session.query(Task) \
    .filter(Task.id == task_id) \
    .delete()
    session.commit()

    return