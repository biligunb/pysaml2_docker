FROM ubuntu:18.04

RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y build-essential && apt-get install -y software-properties-common
RUN apt-get install -y curl git unzip vim wget

RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get install -y pkg-config
RUN apt-get install -y libxmlsec1-dev
RUN apt-get install -y xmlsec1

RUN pip3 install mako
RUN pip3 install cherrypy
RUN pip3 install cryptography==2.2.1

ENV WORKSPACE=pysaml2

RUN mkdir $WORKSPACE
RUN git clone https://github.com/IdentityPython/pysaml2.git
WORKDIR $WORKSPACE

RUN python3 setup.py install
RUN ln -s /usr/bin/python3.6 /usr/bin/python

ADD idp_conf.py example/idp2/idp_conf.py
ADD sp_conf.py example/sp-wsgi/sp_conf.py
ADD service_conf.py example/sp-wsgi/service_conf.py

RUN cd example/sp-wsgi/ && pwd && ls && make_metadata.py sp_conf.py > sp.xml
RUN cd example/idp2/ && pwd && ls && make_metadata.py idp_conf.py > idp.xml

EXPOSE 8087
EXPOSE 8088
