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
    $ docker run -it -p 8088:8088 -p 5000:5000 --rm bubuntu
    ```
   - 5000 for SP (Flask example)
   - 8088 for IdP (PySAML2.0 example)

##### Start services SP & IdP
 - Flask example (Start SP)
   ```
   $ cd example/sp
   $ ./python app.py
   ```

 - In different bash (Start IdP)
   - docker ps
   - docker exec -it <DOCKER_CONTAINER_ID> /bin/bash
   ```
   $ cd example/idp2
   $ ./idp.py idp_conf &
   ```

##### Check in browser
 - Go to browser and type
   - http://localhost:5000
   - Username : roland
   - Password : dianakra

   > Step 1. Go to SP (http://localhost:5000)  
   > Step 2. will be redirected to IdP login page (https://localhost:8088/sso/redirect?SAMLRequest=xxxx)  
   > Step 3. Provide login information  
   > Step 4. Successful login will be redirected to (http://localhost:5000/user)  
