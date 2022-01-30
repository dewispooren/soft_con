# soft_con

## Get the most recent version
```bash
git clone https://github.com/dewispooren/soft_con.git
```
Go to directory
```bash
cd Documents/soft_con
```

## create an environment 

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

## deploy postgresql (only once)
```bash
kubectl apply -f postgres-config.yaml 
```
```bash
kubectl apply -f postgres-secret.yaml 
```
```bash
sudo mkdir -p /opt/postgre/data 
```
```bash
kubectl apply -f postgres-storage.yaml 
```
```bash
kubectl apply -f postgres-deployment.yaml 
```
```bash
kubectl apply -f postgres-service.yaml 
```

## Get cluster-IP address of postgres-service
```bash
kubectl get svc
```
store cluster-IP address
Go to file config.py in src folder.
change the cluster-IP in SQLALCHEMY_DATABASE_URI into the right cluster-IP


## create the tables in database
first delete migrations folder

```bash
python manage.py db init
```
```bash
python manage.py db migrate
```
```bash
python manage.py db upgrade
```

## access postgresql from client on host
Use the correct cluster-IP in the command:
```bash
psql -h 10.152.183.122 -U postgresadmin -p 5432 postgresdb
```
password is admin123

## create a docker image 

- sudo docker build . 
- sudo docker images 
- sudo docker tag image_id new_image_id 
- sudo docker run -p 5000:5000 new_image_id 
- load the URL: http://0.0.0.0:5000/api/v1/blog

## push the image to the microk8s registry

- sudo docker tag image_id localhost:32000/image_id:v1
- microk8s start
- microk8s enable registry
- sudo docker push localhost:32000/inventory-api:v1

## create a Kubernetes deployment 

in deployment file
- make sure that the image is the same as the image you just created (localhost:32000/image_id:v1)

- kubectl apply -f softcon-deployment.yaml
- kubectl get pods -l app=softcon

## create a kubernetes service of type clusterIP 
- kubectl apply -f inventory-api-service.yaml
- kubectl get svc
- load the url: http://"cluster-ip":8081/inventory/api/v1/blog

## post request
Download tool postman
create a new collection and a new request
select the method post and raw data of type JSON
add new user

## rebuild image after changing a file
get container id
```bash
docker ps -a
```
```bash
docker rm -f <container_id>
```
check if image is deleted
```bash
sudo docker images
```
and then you can build again
