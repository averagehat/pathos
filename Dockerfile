FROM centos:centos7
MAINTAINER Michael Panciera

ENV PYTHON_VERSION 3.7

RUN yum -y update \
    && yum -y install curl bzip2 git wget make gcc-c++ \
    && curl -sSL https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o /tmp/miniconda.sh \ 
    && bash /tmp/miniconda.sh -bfp /usr/local/ \
    && rm -rf /tmp/miniconda.sh \
    && conda install -y python=$PYTHON_VERSION \
    && conda update conda \
    && conda clean --all --yes \
    && rpm -e --nodeps curl bzip2 \
    && yum clean all

ENV PATH "/usr/local/bin/:$PATH"

ENV RUNTYPE "TEST"
ADD . /app
WORKDIR /app

RUN    cd install \
    && sh assume-conda-install.sh /usr/local/bin/ \ 
    && cd .. \
    && sh mk_yaml.sh > test.yaml \
    && cd databases \
    && sh test-setup.sh \
    && pip install -r ../install/test-requirements.txt 
