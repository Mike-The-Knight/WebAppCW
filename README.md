# WebAppCW
Group 18 - Web App coursework


# Docker
## Docker commands to run
First run the following:
```
docker build -t my-django-app .
```
This will build the docker locally, you must have Docker Desktop running.

Then run:
```
docker run -it -p 8000:8000 my-django-app
```
This will start the app on your local host.
