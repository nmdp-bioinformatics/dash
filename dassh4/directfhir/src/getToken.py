#!/usr/bin/env python3
"""CIBMTR uses OAuth2.0/OpenID (OIDC) for authentication and access management.
This reads a json file containing authorization parameters and POSTs a
request to a third-party authorization server to receive a token.
"""
__version__ = '1.0'
__author__ = 'Bob Milius'
__copyright__ = 'Copyright (c) 2021 National Marrow Donor Program'
__license__ = 'Apache 2.0'

import requests
import json
from requests.auth import HTTPBasicAuth


def main():
    # authorizaiton parameters are found in json file
    # {
    #     "username": "CIBMTR Service Account Username",
    #     "password": "CIBMTR Service Account Password",
    #     "clientId": "Application Client ID",
    #     "clientSecret": Application Client Secret",
    #     "clientScope": "Application Scope"
    # }

    with open('authparam.json', 'r') as infile:
        authparam = json.load(infile)

    headers = {'Content-Type': 'application/x-www-form-urlencoded',
               'Accept': 'application/json'}

    data = {'grant_type': 'password',
            'scope': authparam['clientScope'],
            'username': authparam['username'],
            'password': authparam['password']
            }

    r = requests.post('https://nmdp.oktapreview.com/oauth2/ausaexcazhLhxKnJs0h7/v1/token',
                      auth=HTTPBasicAuth(
                          authparam['clientId'], authparam['clientSecret']),
                      data=data,
                      headers=headers)

    accessToken = r.json()["access_token"]
    print(accessToken, end='')


if __name__ == '__main__':
    main()
