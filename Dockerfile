FROM tensorflow/tensorflow:latest-py3
MAINTAINER Spencer Chen
RUN pip install --upgrade pip
RUN pip install -q tensorflow==2.0.0-beta1
RUN pip install matplotlib
