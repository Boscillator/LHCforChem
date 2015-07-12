ENV port 80
ENV gitRepo https://github.com/Boscillator/LHCforChem.git

FROM ubuntu:14.04
RUN apt-get upgrade
RUN apt-get install python-pip python-dev build-essential
RUN apt-get install git

RUN pip install flask

EXPOSE $port

WORKDIR /code
git clone $gitRepo

CMD /code/production.py