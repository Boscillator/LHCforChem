FROM ubuntu:14.04

ENV port 80
ENV gitRepo https://github.com/Boscillator/LHCforChem.git


RUN apt-get update
RUN apt-get -y install python-pip python-dev build-essential
RUN apt-get -y install git

RUN pip install flask

EXPOSE $port

ADD . /code
RUN ls

WORKDIR /code
CMD python /code/production.py