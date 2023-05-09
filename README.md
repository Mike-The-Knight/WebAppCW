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

# Testing
## To run tests
Find the container ID or name for the MySQL container created by docker:
```
docker ps
```
Run an interactive shell in the container:
```
docker exec -it CONTAINER_ID_OR_NAME bash
```
Start the mysql command-line client as the root user:
```
mysql -u root -p
```
Enter the root password when prompted (MYSQL2505, as is stated in our docker-compose).

Run the SQL commands to grant the necessary privileges:
```
GRANT ALL PRIVILEGES ON `test_%`.* TO 'MichaelBAW'@'%';

FLUSH PRIVILEGES;
```
Now, run the following to test:

```
docker-compose run web python manage.py test website

docker-compose run web python manage.py test members
```

