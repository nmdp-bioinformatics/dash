#!/usr/bin/env python3

import sys
import json
import requests
from pathlib import Path

if len(sys.argv) < 2:
    sys.exit("Usage: python postObservation.py <FHIR Observation resource json file>")
fhirjsonfile = Path(sys.argv[1])
observation = fhirjsonfile.read_text()

# Bearer token captured in token.txt
tokenfile = Path('token.txt')
authstring = 'Bearer ' + tokenfile.read_text()
headers = {'Authorization': authstring}

r = requests.post('https://dev-api.nmdp.org/cibmtrehrclientbackendexttest/v1/r3/Observation',
                  data=observation,
                  headers=headers)
if r:
    # print(json.dumps(r.json(), indent=4))
    print(r.headers['Location'])
    print(r.text)
else:
    print(r.status_code)
    print(r.headers)
    print(r.text)
