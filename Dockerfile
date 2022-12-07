From python:3.10
ENV PYTHONBUFFERED 1
RUN mkdir /src
WORKDIR /src
COPY ./netflixprj /src
RUN pip install --trusted-host pypy.org --trusted-host files.pythonhosted.org -r requirements.txt
FROM nginx:stable-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY ./nginx/nginx.conf /etc/nginx/conf.d
