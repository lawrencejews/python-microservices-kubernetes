### Python-Microservices
- Create a virtual-env `python3 -m venv venv`.
- Activate your environment `source ./venv/bin/activate`.
- Access your sql shell using this command for password prompt `mysql -u root -p  `.
#### Docker Images
- Auth service docker images: `docker build .` , `docker tag XXXXXX lawrencejews/auth:latest` and `docker push lawrencejews/auth:latest`.
- Deploy Auth image to Kubernetes cluster for the manifest dir `kubectl apply -f ./` & Clean up `kubectl delete -f ./   `.