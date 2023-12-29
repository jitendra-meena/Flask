from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

api = Api(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import views, models, resources

# Add resources to the Flask-RESTful API
api.add_resource(resources.TaskResource, '/tasks/<int:task_id>')
api.add_resource(resources.TaskListResource, '/tasks')