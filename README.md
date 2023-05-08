# WebAppCW
Group 18 - Web App coursework


# Docker
## Docker commands to run
First run the following:
```
docker-compose build web

docker-compose build chat
```
This will build the docker locally, you must have Docker Desktop running.

Then create the database:
```
docker-compose run web python manage.py migrate
```

Then run:
```
docker-compose up
```
This will start the app on your local host.
