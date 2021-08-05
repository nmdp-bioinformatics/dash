#!/bin/bash
auth_string="Bearer $(./getToken.py)"
#
echo ${auth_string}
curl --location --request PUT 'https://dev-api.nmdp.org/cibmtrehrclientbackendexttest/v1/CRID' \
--header "Authorization: ${auth_string}" \
--header 'Content-Type: application/json' \
--data-raw '{
    "ccn": "12002",
    "patient": {
        "firstName": "John",
        "lastName": "Roger",
        "birthDate": "1926-07-01",
        "gender": "M"
    }
}'