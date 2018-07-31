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
