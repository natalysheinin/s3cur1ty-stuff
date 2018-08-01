FROM alpine:3.7

RUN mkdir -p /home/myapp

RUN addgroup -S -g 123456 myapp &&\
    adduser -S -u 123456 -G myapp myapp

ENV HOME=/home/myapp

WORKDIR $HOME

COPY entrypoint.sh /home/myapp/entrypoint.sh

RUN chown -R myapp:myapp $HOME
RUN chmod +x $HOME/entrypoint.sh

USER 123456:123456

ENTRYPOINT [ "/home/myapp/entrypoint.sh" ]
