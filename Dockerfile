FROM ubuntu:20.04
RUN apt-get update -y
RUN apt-get install python3 python3-dev python3-pip -y
COPY . /
WORKDIR /
RUN pip3 install -r requirements.txt