from flask_restful import Resource, reqparse
from app.models import Task
from app import db

parser = reqparse.RequestParser()
parser.add_argument('title', type=str, help='Title of the task')
parser.add_argument('description', type=str, help='Description of the task')

class TaskResource(Resource):
    def get(self, task_id):
        task = Task.query.get(task_id)
        if task:
            return {'title': task.title, 'description': task.description}
        return {'message': 'Task not found'}, 404

    def put(self, task_id):
        args = parser.parse_args()
        task = Task.query.get(task_id)
        if task:
            task.title = args['title']
            task.description = args['description']
            db.session.commit()
            return {'message': 'Task updated successfully'}
        return {'message': 'Task not found'}, 404

    def delete(self, task_id):
        task = Task.query.get(task_id)
        if task:
            db.session.delete(task)
            db.session.commit()
            return {'message': 'Task deleted successfully'}
        return {'message': 'Task not found'}, 404

class TaskListResource(Resource):
    def get(self):
        tasks = Task.query.all()
        return [{'title': task.title, 'description': task.description} for task in tasks]

    def post(self):
        args = parser.parse_args()
        task = Task(title=args['title'], description=args['description'])
        db.session.add(task)
        db.session.commit()
        return {'message': 'Task created successfully'}
