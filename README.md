### Python-Microservices with Kubernetes and RabbitMQ.
- Create a virtual-env `python3 -m venv venv`.
- Activate your environment `source ./venv/bin/activate`.
- Check the project working environment ` env | grep ENV  `.
- Access your sql shell using this command for password prompt `mysql -u root -p  `.
#### Auth
- Create an Environment with `pyjwt`,`flask`and `flask_mysqldb`.
- Create a requirement.txt `pip3 freeze > requirement.txt`.
#### Gateway
- Create an Environment with `pika`,`requests`,`flask`, `pyMongo`and `Flask-PyMongo`.
- Create a requirement.txt `pip3 freeze > requirement.txt`.
- Map localhost for requests with minikube `/etc/hosts` by adding a loopback address with ingress at `127.0.0.1 mp3converter.com` spec host.
- Check if ingress is enabled `minikube addons list` or Enable ingress on minikube `minikube addons enable ingress`.
- Run the tunnel `minikube tunnel` and ingress resources would be available on address `127.0.0.1`.
#### RabbitMQ
- The producer `gateway` through the exchange queries for `login, validation, queuing` messages before passing them to the consumer `converter`.
- Map localhost for requests with minikube `/etc/hosts` by adding a loopback address with ingress at `127.0.0.1 rabbitmq-manager.com` spec host.
- Run the tunnel `minikube tunnel` and ingress resources would be available on address `127.0.0.1`.
#### Converter 
- The consumer requesting messages from the broker queue to convert videos to mp3 `moviepy`.
- Create videos and mp3 queues with RabbitMQ: NOTE -> start the minikube tunnel before connecting to the internals.
#### Docker Images
- Auth service docker images: `docker build .` , `docker tag XXXXXX lawrencejews/auth:latest` and `docker push lawrencejews/auth:latest`.
- Deploy Auth image to Kubernetes cluster from the manifests `kubectl apply -f ./` & Clean up `kubectl delete -f ./   `.
- To Scale down your deployment `kubectl scale deployment --replicas=XX gateway`.