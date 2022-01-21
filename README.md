# soft_con

## create an environment 
in subdirectory inventory-api:
```bash
python -m venv venv
```

## activate the environment
```bash
$ . venv/bin/activate
```
On Windows:
```bash
venv\Scripts\activate
```

## install libraries from requirements.txt

```bash
pip install -r requirements.txt
```

## Automatically update requirements.txt

If you download new libraries, you should update requirements.txt

```bash
pip freeze > requirements.txt 
```

## created a docker image for flask API application

in subdirectory inventory-api:
- sudo docker build . 
- sudo docker images 
- sudo docker tag ... inventory-app:v1 
- sudo docker run -p 5000:5000 inventory-app:v1 
- load the URL: http://localhost:5000/inventory/api/v1.0/book/

## push the image to the microk8s registry

- sudo docker tag inventory-app:v1 localhost:32000/inventory-api:v1
- microk8s start
- microk8s enable registry
- sudo docker push localhost:32000/inventory-api:v1

## create a Kubernetes deployment for the flask APO

in main directory
- kubectl apply -f inventory-api-deployment.yaml
- kubectl get pods -l app=inventory-api

## create a kubernetes service of type clusterIP for the Flask API
- kubectl apply -f inventory-api-service.yaml
- kubectl get svc
- load the url: http://"cluster-ip":8081/inventory/api/v1.0/books


# Create persistent layer using PostgreSQL database

## create configuration file for storing PostgreSQL related information
```bash
kubectl apply -f postgres-config.yaml
```
## Create a secret file to encode the password using base64 
```bash
kubectl apply -f postgres-secret.yaml
```
## create storage file to save the data on a persistent storage
make a directory
```bash
sudo mkdir -p /opt/postgre/data
```
```bash
kubectl apply -f postgres-storage.yaml
```
## create deployment file 
```bash
kubectl apply -f postgres-deployment.yaml
```
## create service file to acces the deployment or container using CLusterIP
```bash
kubectl apply -f postgres-service.yaml
```

## connect to PostgreSQL
ensure that the Postgres client is installed
```bash
sudo apt install postgresql-client
```
connect to PostgreSQL from machine
```bash
psql -h localhost -U postgresadmin --password -p 30001 postgresdb
```
password is password from secret file (admin123)

To show list of databases
```bash
\l
```

To show list of relations
```bash
\dt
```

# Sample API

## Install packages 
```bash
sudo apt-get install pipenv
```
```bash
sudo apt-get install libpq-dev python3-dev
```

## activate environment
```bash
pipenv shell
```
```bash
pipenv install
```

## set environment variables
```bash
export FLASK_ENV=development
```
```bash
export DATABASE_URL=postgres://postgresadmin:admin123@localhost:30001/postgresdb
```

## install postgres client
```bash
sudo apt install postgresql-client-common postgresql-client
```
## execute creation of the tables in database
```bash
mv migrations migrations.old
```
```bash
python manage.py db init
```
```bash
python manage.py db migrate
```
```bash
python manage.py db upgrade
```
```bash
psql -h localhost -U
postgresadmin -p 30001 postgresdb
```

open browser on:
http://0.0.0.0:5000/api/v1/users/

## post request
Download tool postman
create a new collection and a new request
select the method post and raw data of type JSON
add new user

