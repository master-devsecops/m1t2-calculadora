FROM alpine:3.12

WORKDIR /m1t2-calculadora

ADD . /m1t2-calculadora

RUN apk add python3

