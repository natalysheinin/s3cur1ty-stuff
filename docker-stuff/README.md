## Simple instructions for running a docker container as non-root

1. Create a Dockerfile:
```
FROM alpine:latest

RUN mkdir -p /home/myapp

RUN addgroup -S -g 123456 myapp &&\
    adduser -S -u 123456 -G myapp myapp

ENV HOME=/home/myapp
WORKDIR $HOME

USER 123456:123456
```

2. Create the image
`docker build -t=alpine_nonroot .` 

3. Does image exist?
`docker images`

4. Run the container & replace image id
`docker run -it --rm c95580101aa6 /bin/sh`

5. Check the USER column in the process list
`ps` 

## Running this on kubernetes - minikube

1. Prereq: have minikube installed

2. `minikube start`

3. `eval $(minikube docker-env)`

4. Create the image again: `docker build -t=alpine_nonroot .` 

5. `k create -f alpine_deploy.yaml` 

6.  `k exec` into your pod or container and try to escalate privilege 
