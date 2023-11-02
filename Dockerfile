FROM alpine:3.12
# Definir variables de entorno
ENV NOMBRE "CAL24"

WORKDIR /m1t2-calculadora

ADD . /m1t2-calculadora

RUN apk add python3

