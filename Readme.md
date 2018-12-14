# Dockerized version of PySAML2 (`pysaml2_docker`)
[![biligunb](https://i.imgur.com/kwl63Eb.jpg)](https://medium.com/@biligunb)

### `pysaml2_docker` is a dockerized version of [PySAML2](https://github.com/IdentityPython/pysaml2) library.
 - Ubuntu:18.04
 - Customized to expose Docker to host

### Help
##### Docker build
 - from main directory run
    ```sh
    $ docker build -t bubuntu .
    ```

##### Docker run
 - from main directory run
    ```sh
    $ docker run -it -p 8088:8088 -p 8087:8087 --rm bubuntu
    ```
   - 8087 for SP
   - 8088 for IdP

##### Start services SP & IdP
 - Go to example directory and run
    ```sh
    $ cd example
    $ ./all.sh start
    ```
 - IdP only
   ```
   $ ./idp.py idp_conf &
   ```

##### Check in browser
 - Go to browser and type
   - http://localhost:8087
   - Username : roland
   - Password : dianakra

   > Step 1. Go to SP (http://localhost:8087)  
   > Step 2. will be redirected to IdP login page (https://localhost:8088/sso/redirect?SAMLRequest=xxxx)  
   > Step 3. Provide login information  
   > Step 4. Successful login will be redirected to (http://localhost:8087/acs/post)  

### Bugs
  - Error after SSO login
    - cheroot/server.py : `ValueError: WSGI Applications must yield bytes`
