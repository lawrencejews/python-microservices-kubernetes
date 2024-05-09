### Python-Microservices with Kubernetes and RabbitMQ.
- Create a virtual-env `python3 -m venv venv`.
- Check the project working environment ` env | grep ENV  `.
- Activate your environment `source ./venv/bin/activate`.
- Access your sql shell using this command for password prompt `mysql -u root -p  `.
#### Auth
- Create an Environment with `pyjwt`, `flask`,  and `flask_mysqldb`.
- Create a requirement.txt `pip3 freeze > requirement.txt`.
#### Gateway
- Create an Environment with `pika`,`requests`, `flask`, `pyMongo` and `Flask-PyMongo`.
- Create a requirement.txt `pip3 freeze > requirement.txt`.
- Localhost tunneling of requests with minikube `/etc/hosts` then map the loopback address with your ingress `127.0.0.1 mp3converter.com` spec host.
- Check if ingress is enabled `minikube addons list` or Enable ingress on minikube `minikube addons enable ingress`.
- Run the tunnel `minikube tunnel` and ingress resources would be available at `127.0.0.1`.
#### Docker Images
- Auth service docker images: `docker build .` , `docker tag XXXXXX lawrencejews/auth:latest` and `docker push lawrencejews/auth:latest`.
- Deploy Auth image to Kubernetes cluster for the manifest dir `kubectl apply -f ./` & Clean up `kubectl delete -f ./   `.
- To Scale down your deployment `kubectl scale deployment --replicas=XX gateway`.