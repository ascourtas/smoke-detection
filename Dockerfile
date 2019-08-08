FROM tensorflow/tensorflow:latest-py3
MAINTAINER Spencer Chen
RUN apt update && \
apt install -y nano
RUN pip install --upgrade pip
RUN pip install tensorflow==2.0.0-beta1 && \
pip install matplotlib && \
pip install jupyter notebook