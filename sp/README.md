# Introduction

This is an example SAML SP service written using [Flask](http://flask.pocoo.org/) and [pysaml2](https://github.com/rohe/pysaml2).

# Requirements
-   [Python](https://www.python.org/) 3.6+
-   [Virtualenv](https://virtualenv.pypa.io/en/latest/)
-   [pip](https://pip.pypa.io/en/stable/)

You will also need a development environment capable of compiling
Python packages and the "libffi" and "libxmlsec1" development
libraries, which are needed by PySAML2.

Instructions for installing these development libraries will differ
depending on your host operating system.

```shell
$ sudo apt-get install -y libffi-devel xmlsec1 xmlsec1-openssl memcached python-memcached
```

# Installation

```shell
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

# Running

 ```shell
$ python app.py 
 ```

# Testing Saruuls's Idp

    Edit the "app.py" file and uncomment the line in the "test" line in "metadata\_url\_for" dictionary.
    
    ```shell
    $ $EDITOR app.py
    ```
    ```on the browser
    $ choose idp
	username: roland
	password: dianakra
    ```

# Testing OKTA public Idp

The fastest way to test this example SAML SP is to use the [saml.oktadev.com](http://saml.oktadev.com/) service.

Here is how:

1.  Edit the "app.py" file and uncomment the line in the "test" line in "metadata\_url\_for" dictionary.
    
    ```shell
    $ $EDITOR Hello.py
    ```
    
    Change this line:
    
    ```shell
    # 'test': 'http://idp.oktadev.com/metadata',                                                                                                
    ```
    
    To this:
    
    ```shell
    'test': 'http://idp.oktadev.com/metadata',
    ```
2.  Start the example SAML SP
    
    ```shell
    $ python app.py
    ```
3.  Start ngrok on the port that the example SAML SP is running on. By default, the example SAML SP runs on TCP 5000.
    
    ```shell
    $ ngrok http 5000
    ```
    
    You will need to [install ngrok](https://ngrok.com/download) if you haven't already.
    
    Here is what it should look like:
    
    ![img](./docs/_static/ngrok.png "A screenshot of ngrok 2.0 running")
4.  Run [saml.oktadev.com](http://saml.oktadev.com) to test this example SAML SP
    -   Load [saml.oktadev.com](http://saml.oktadev.com) in your browser and fill out as follows:
        
        **Issuer:** "urn:example:idp"
        
        **SAML ACS URL:** "<http://REPLACE_ME.ngrok.io/saml/sso/test>"
        
        **SAML Audience URI:** "<http://REPLACE_ME.ngrok.io/saml/sso/test>"
        
        Be sure to replace the string "REPLACE\_ME" with the sub-domain that ngrok selected for you!
    -   Click the "Submit" button.
    -   Your output should look like the image below:
        ![img](./docs/_static/validation-success.png)
