FROM alpine:latest

RUN mkdir /app

COPY seedApp /app

CMD ["/app/seedApp"]