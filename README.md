# soft_con

## created a docker image for flask API application

in subdirectory inventory-api:
- sudo docker build . >build the image
- sudo docker images >get tag from IMAGE ID
- sudo docker tag ... inventory-app:v1 >tag image to get meaningful name
- sudo docker run -p 5000:5000 inventory-app:v1 >test application
- load the URL: https://localhost:5000/inventory/api/v1.0/books

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


