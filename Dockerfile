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
ENV LC_ALL C.UTF-8
ENV LANG en_US.UTF-8

RUN mkdir $WORKSPACE
RUN git clone https://github.com/IdentityPython/pysaml2.git
WORKDIR $WORKSPACE

RUN python3 setup.py install
RUN ln -s /usr/bin/python3.6 /usr/bin/python

ADD idp/idp_conf.py example/idp2/idp_conf.py
ADD idp/idp.py example/idp2/idp.py
#RUN cd example/idp2/ && pwd && ls && make_metadata.py idp_conf.py > idp.xml
ADD idp/idp.xml example/idp2/idp.xml
ADD sp/sp.xml example/idp2/sp.xml

RUN mkdir example/sp
ADD sp/requirements.txt example/sp/requirements.txt
RUN cd example/sp && pip3 install -r requirements.txt
ADD sp/ example/sp/

RUN cd example/sp && set FLASK_APP=app.py
RUN cd example/sp && set FLASK_ENV=development

EXPOSE 5000
EXPOSE 8087
EXPOSE 8088
