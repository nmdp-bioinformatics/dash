#!/usr/bin/env python3
"""Takes patient demographics data found in a json file, and PUTs it to the
externally available CIOBMTR CRID endpoint.
If the patient already exists, the CRID is returned. 
If the patient does not already exist, a new CRID is created and is returned.
"""
__version__ = '1.0'
__author__ = 'Bob Milius'
__copyright__ = 'Copyright (c) 2021 National Marrow Donor Program'
__license__ = 'Apache 2.0'


import sys
import json
import requests
from pathlib import Path


def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: python getCRID.py <patient json file>")

    # the patient file contains a json object that conforms to the following structure:
    # {
    #     "ccn": "string",
    #     "patient": {
    #         "firstName": "string",
    #         "lastName": "string",
    #         "birthDate": "string",
    #         "gender": "string",
    #         "ssn": "string",
    #         "mothersMaidenName": "string",
    #         "race": ["string"],
    #         "ethnicity": "string",
    #         "nmdpRid": 0,
    #         "ebmtCic": "string",
    #         "cibmtrIubmid": "string",
    #         "cibmtrTeam": 0,
    #         "ebmtId": "string"
    #     }
    # }

    patientfile = Path(sys.argv[1])
    patient = patientfile.read_text()
    # Bearer token was captured in token.txt
    # see getCRID.py
    tokenfile = Path('token.txt')
    authstring = 'Bearer ' + tokenfile.read_text()

    headers = {'Authorization': authstring,
               'Content-Type': 'application/json'}

    r = requests.put('https://dev-api.nmdp.org/cibmtrehrclientbackendexttest/v1/CRID',
                     data=patient,
                     headers=headers)
    if r:
        if r.status_code == 200:
            print(r.json()['perfectMatch'][0]['crid'])
        elif r.status_code == 201:
            print(r.json()['crid'])
        else:
            print("status code = " + r.status_code)
        print(json.dumps(r.json(), indent=4))
    else:
        print(r.status_code)


if __name__ == '__main__':
    main()
