#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os.path

from saml2 import BINDING_HTTP_REDIRECT, BINDING_URI
from saml2 import BINDING_HTTP_ARTIFACT
from saml2 import BINDING_HTTP_POST
from saml2 import BINDING_SOAP
from saml2.saml import NAME_FORMAT_URI
from saml2.saml import NAMEID_FORMAT_TRANSIENT
from saml2.saml import NAMEID_FORMAT_PERSISTENT

try:
    from saml2.sigver import get_xmlsec_binary
except ImportError:
    get_xmlsec_binary = None

if get_xmlsec_binary:
    xmlsec_path = get_xmlsec_binary(["/opt/local/bin"])
else:
    xmlsec_path = '/usr/bin/xmlsec1'

BASEDIR = os.path.abspath(os.path.dirname(__file__))


def full_path(local_file):
    return os.path.join(BASEDIR, local_file)

HOST = '0.0.0.0'
PORT = 8088

HTTPS = False

if HTTPS:
    BASE = "https://%s:%s" % (HOST, PORT)
    BASE_BEBI = "https://%s:%s" % ('localhost', PORT)
else:
    BASE = "http://%s:%s" % (HOST, PORT)
    BASE_BEBI = "http://%s:%s" % ('localhost', PORT)

# HTTPS cert information
SERVER_CERT = "pki/mycert.pem"
SERVER_KEY = "pki/mykey.pem"
CERT_CHAIN = ""
SIGN_ALG = None
DIGEST_ALG = None
#SIGN_ALG = ds.SIG_RSA_SHA512
#DIGEST_ALG = ds.DIGEST_SHA512


CONFIG = {
    "entityid": "http://idp.local",
    "description": "My IDP",
    "valid_for": 168,
    "service": {
        "idp": {
            "name": "Rolands IdP",
            "endpoints": {
                "single_sign_on_service": [
                    ("%s/sso/redirect" % BASE_BEBI, BINDING_HTTP_REDIRECT),
                    ("%s/sso/post" % BASE_BEBI, BINDING_HTTP_POST),
                    ("%s/sso/art" % BASE_BEBI, BINDING_HTTP_ARTIFACT),
                    ("%s/sso/ecp" % BASE_BEBI, BINDING_SOAP)
                ],
                "single_logout_service": [
                    ("%s/slo/soap" % BASE_BEBI, BINDING_SOAP),
                    ("%s/slo/post" % BASE_BEBI, BINDING_HTTP_POST),
                    ("%s/slo/redirect" % BASE_BEBI, BINDING_HTTP_REDIRECT)
                ]
            },
            "policy": {
                "default": {
                    "lifetime": {"minutes": 15},
                    "attribute_restrictions": None, # means all I have
                    "name_form": NAME_FORMAT_URI,
                    "entity_categories": ["swamid", "edugain"]
                },
            },
            "subject_data": "./idp.subject",
            "name_id_format": [NAMEID_FORMAT_TRANSIENT,
                               NAMEID_FORMAT_PERSISTENT]
        },
    },
    "debug": 1,
    "key_file": full_path("pki/mykey.pem"),
    "cert_file": full_path("pki/mycert.pem"),
    "metadata": {
        "local": [full_path("../idp2/sp.xml")],
    },
    "organization": {
        "display_name": "Rolands Identiteter",
        "name": "Rolands Identiteter",
        "url": "http://www.example.com",
    },
    "contact_person": [
        {
            "contact_type": "technical",
            "given_name": "Roland",
            "sur_name": "Hedberg",
            "email_address": "technical@example.com"
        }, {
            "contact_type": "support",
            "given_name": "Support",
            "email_address": "support@example.com"
        },
    ],
    # This database holds the map between a subject's local identifier and
    # the identifier returned to a SP
    "xmlsec_binary": xmlsec_path,
    #"attribute_map_dir": "../attributemaps",
    "logger": {
        "rotating": {
            "filename": "idp.log",
            "maxBytes": 500000,
            "backupCount": 5,
        },
        "loglevel": "debug",
    }
}

# Authentication contexts

    #(r'verify?(.*)$', do_verify),

CAS_SERVER = "https://cas.umu.se"
CAS_VERIFY = "%s/verify_cas" % BASE
PWD_VERIFY = "%s/verify_pwd" % BASE

AUTHORIZATION = {
    "CAS" : {"ACR": "CAS", "WEIGHT": 1, "URL": CAS_VERIFY},
    "UserPassword" : {"ACR": "PASSWORD", "WEIGHT": 2, "URL": PWD_VERIFY}
}
