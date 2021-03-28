from flask import Flask
from flask_restful import Api, Resource

def create_app(test_config=None):
    app = Flask(__name__)
    api = Api(app)

    if test_config == None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.update(test_config)

    from src.db import init_app
    init_app(app)

    from src.task.controller import task, tasks, task_by_id

    api.add_resource(task.TaskController, "/task", endpoint="task")
    api.add_resource(task_by_id.TaskByIdController, "/task/<int:task_id>", endpoint="task_by_id")
    api.add_resource(tasks.TasksController, "/tasks", endpoint="tasks")

    @app.route('/')
    def hello_world():
        """Print 'Hello, world!' as the response body."""
        return 'Hello, world!'
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0')
