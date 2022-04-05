# ai-sre-interview
Docker and application files for AI Engine SRE interview.

This repo serves as a simple containerized web application, with no persistent storage requirements or external dependencies. One of the containers serves the application frontend code, and the other containers serve backend APIs.

## Prerequisites
Aside from cloning the project repository, the one pre-requisite is that you install [Docker](https://docs.docker.com/get-docker/). We will be using `docker compose` to run the containers.

## Running

You will start the application from within the project directory with this command, which runs the containers in the background:
```
docker compose up --detach
```

## Access

You can then go to http://localhost:8000 in your browser to view the application.

The default endpoint, `/`, serves a simple web application with a broken button. It is your job to fix the web app. 

## Containers

You can list the running containers with the command:
```
docker container ls
```

## Logs

To view the console logs for a given container, use the command:
```
docker logs -f <container_name>
```

