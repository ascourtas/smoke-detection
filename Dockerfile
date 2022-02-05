ARG cuda_version=10.1
ARG cudnn_version=7
FROM nvidia/cuda:${cuda_version}-cudnn${cudnn_version}-devel

ENV NB_USER kerasTester
ENV NB_UID 1000
# RUN mkdir /userdata/kerasData

RUN apt-get update && \
      apt-get -y install sudo

RUN useradd -m -s /bin/bash -N -u $NB_UID $NB_USER && \
    # chown $NB_USER $CONDA_DIR -R && \
    # chown $NB_USER /userdata/kerasData -R && \
    #    chown $NB_USER / -R && \
    # mkdir -p / && \
    sh -c 'echo "$NB_USER:test" | chpasswd' && \
    usermod -aG sudo $NB_USER

WORKDIR /userdata/kerasData

# Install system packages
RUN apt-get update && apt-get install -y --no-install-recommends \
      bzip2 \
      g++ \
      git \
      graphviz \
      libgl1-mesa-glx \
      libhdf5-dev \
      openmpi-bin \
      xvfb \
      screen \
      wget && \
    rm -rf /var/lib/apt/lists/* && mkdir /userdata/kerasData/output

# Install conda
ENV CONDA_DIR /opt/conda
ENV PATH $CONDA_DIR/bin:$PATH

RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-4.7.12.1-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh && \
    /opt/conda/bin/conda clean -tipsy && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate base" >> ~/.bashrc

# Install Python packages and keras

ARG python_version=3.6

RUN conda config --append channels conda-forge
# may need to install cntk-gpu with Conda instead :/ should also try larger EC2 instance in case it was a storage thing
RUN conda install -y python=${python_version} && \
    pip install --upgrade pip && \
    pip install \
      sklearn_pandas \
      opencv-python \
      tensorflow-gpu \
      cntk-gpu && \
    conda install \
      bcolz \
      h5py \
      statsmodels \
      matplotlib \
      mkl \
      nose \
      notebook \
      Pillow \
      pandas \
      pydot \
      pygpu \
      pyyaml \
      scikit-learn \
      six \
      theano \
      mkdocs \
      numpy=1.18

RUN pip install keras

# RUN git clone git://github.com/keras-team/keras.git /src && pip install -e /src[tests]
RUN conda clean -yt
    # pip install git+git://github.com/keras-team/keras.git && \

USER $NB_USER

#ADD theanorc /home/keras/.theanorc

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

ENV PYTHONPATH='/src/:$PYTHONPATH'

COPY ./imageLoader.py /userdata/kerasData

#RUN jupyter trust ./ClassificationExample.ipynb

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=9000"]