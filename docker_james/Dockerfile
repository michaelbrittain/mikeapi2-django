FROM python:3.5
MAINTAINER Mike Brittain
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code

RUN apt-get update && \
 apt-get -y install python curl unzip && \
 cd /tmp && \
 curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-bundle.zip" && \
 unzip awscli-bundle.zip && \
 ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws && \
 rm awscli-bundle.zip && \
 rm -rf awscli-bundle

ADD requirements.txt /code/
RUN pip install -r requirements.txt

ADD . /code/

CMD ["./docker-entrypoint.sh"]
