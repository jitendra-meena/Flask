# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the contents of the local src directory to the container
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Set the environment variable for Flask
ENV FLASK_APP=run.py

# Run the Flask application when the container launches
CMD ["flask", "run", "--host=0.0.0.0"]
