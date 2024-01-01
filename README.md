# Flask CRUD Application with Docker

This is a simple Python Flask application that demonstrates CRUD (Create, Read, Update, Delete) operations using Flask-RESTful. The application is containerized using Docker for easy deployment.

## Prerequisites

Before you begin, ensure you have the following installed:

- Docker: [Install Docker](https://docs.docker.com/get-docker/)
- Docker Compose (optional): [Install Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/jitendra-meena/Flask.git
cd flask-crud-docker
```
# Build and Run with Docker

```bash

# Build the Docker image
docker build -t flask-crud-app .

# Run the Docker container
docker run -p 5000:5000 flask-crud-app
```

The Flask application should now be running at http://localhost:5000.

# Application Structure
The project structure is organized as follows:
```bash

app/: The main package containing the Flask application.
__init__.py: Initializes the Flask app and includes common configurations.
views.py: Contains the API endpoints and business logic.
models.py: Defines database models (if used).
resources.py: Defines Flask-RESTful resources.
run.py: The main entry point for running the application.
Dockerfile: Configuration for building the Docker image.
docker-compose.yml: Configuration for running the Docker container (optional).
requirements.txt: Dependencies required for the application.
API Endpoints
GET /tasks: Get a list of all tasks.
GET /tasks/<int:task_id>: Get details of a specific task.
POST /tasks: Create a new task.
PUT /tasks/<int:task_id>: Update details of a specific task.
DELETE /tasks/<int:task_id>: Delete a specific task.

Example usage:

curl http://localhost:5000/tasks
curl http://localhost:5000/tasks/1
curl -X POST -H "Content-Type: application/json" -d '{"title": "New Task", "description": "Task description"}' http://localhost:5000/tasks
curl -X PUT -H "Content-Type: application/json" -d '{"title": "Updated Task", "description": "Updated description"}' http://localhost:5000/tasks/1
curl -X DELETE http://localhost:5000/tasks/1

```

# Dockerfile
The Dockerfile defines the steps to build the Docker image for the Flask application. It includes the necessary dependencies and sets up the environment for running the application.

# Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.