## Simple instructions for running a docker container as non-root

1. Clone this repo and look at the [`Dockerfile`](https://github.com/natalysheinin/s3cur1ty-stuff/blob/master/docker-stuff/Dockerfile)

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
