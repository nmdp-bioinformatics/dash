#!/usr/bin/env python3

import sys
import json
import requests
from pathlib import Path

if len(sys.argv) < 2:
    sys.exit("Usage: python searchPatientId.py <CRID>")

# Bearer token captured in token.txt
tokenfile = Path('token.txt')
authstring = 'Bearer ' + tokenfile.read_text()
headers = {'Authorization': authstring}

pat_id = sys.argv[1]
security = 'http://cibmtr.org/codesystem/transplant-center|rc_12002'
print(security)
payload = {
    '_id': pat_id,
    '_security': security
}

r = requests.get('https://dev-api.nmdp.org/cibmtrehrclientbackendexttest/v1/r3/Patient',
                 params=payload,
                 headers=headers)
if r:
    # print(json.dumps(r.json(), indent=4))
    print(r.text)
else:
    print(r.status_code)
