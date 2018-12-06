Dockerized version of PySAML2
 - https://github.com/IdentityPython/pysaml2

Changed to use with docker
 - idp_conf.py
 - service_conf.py
 - sp_conf.py

### Docker image build
 - docker build -it bubuntu .
### Docker run with ports exposed
 - docker run -it -p 8088:8088 -p 8087:8087 --rm bubuntu
### Start services SP & IdP
 - cd example && ./all.sh start
### Check in browser
 - http://localhost:8087

#username : roland
#password : dianakra
