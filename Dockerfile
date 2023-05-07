# Use the official Python image as the base image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y netcat

# Install project dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY project /app/project

# Expose the port your Django app runs on
EXPOSE 8000

# Run the Django development server
CMD ["sh", "-c", "python /app/project/manage.py runserver 0.0.0.0:8000"]

