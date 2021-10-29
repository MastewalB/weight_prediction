FROM python:3.6-alpine
MAINTAINER Basilisk
ENV PYTHONBUFFERED 1
RUN apk --no-cache --update-cache add gcc gfortran build-base libpng-dev openblas-dev
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
RUN mkdir /app 
WORKDIR /app
COPY ./app app 
RUN adduser -D user 
USER user 