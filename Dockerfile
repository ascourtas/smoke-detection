FROM tensorflow/tensorflow:latest-gpu-jupyter   
MAINTAINER Spencer Chen
RUN pip install --upgrade pip
RUN pip install -q tensorflow==2.0.0-beta1
