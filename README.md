### Python-Microservices
- Create a virtual-env `python3 -m venv venv`.
- Check the project working environment ` env | grep ENV  `.
- Activate your environment `source ./venv/bin/activate`.
- Access your sql shell using this command for password prompt `mysql -u root -p  `.
#### Auth
- Create an Environment with `pyjwt`, `flask`,  and `flask_mysqldb`.
- Create a requirement.txt `pip3 freeze > requirement.txt`.
#### Gateway
- Create an Environment with `pika`, `flask`, `pyMongo` and `Flask-PyMongo`.
- Create a requirement.txt `pip3 freeze > requirement.txt`.
#### Docker Images
- Auth service docker images: `docker build .` , `docker tag XXXXXX lawrencejews/auth:latest` and `docker push lawrencejews/auth:latest`.
- Deploy Auth image to Kubernetes cluster for the manifest dir `kubectl apply -f ./` & Clean up `kubectl delete -f ./   `.