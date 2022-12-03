From python:3.10
ENV PYTHONBUFFERED 1
RUN mkdir /src
ADD ./netflixprj /src
WORKDIR /src
RUN pip install --trusted-host pypy.org --trusted-host files.pythonhosted.org -r requirements.txt
