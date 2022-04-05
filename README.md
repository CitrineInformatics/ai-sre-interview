# ai-sre-interview
Docker and application files for AI Engine SRE interview.

This repo serves as a very simple containerized web application, with no persistent storage requirements or external dependencies.

## Endpoints

* The default endpoint, `/`, 

## Building

```
docker build -t ai-sre-interview .
```

## Running

```
docker run -it ai-sre-interview
```

You can then go to http://localhost:8000 in your browser to view the application.
