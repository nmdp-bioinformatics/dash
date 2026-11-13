#!/bin/bash
# gets an authorization token for use with CIBMTR Direct FHIR API
#
# uses curl and jq
# https://curl.se/
# https://stedolan.github.io/jq/


# authorizaiton parameters are found in json file
# {
#     "username": "CIBMTR Service Account Username",
#     "password": "CIBMTR Service Account Password",
#     "clientId": "Application Client ID",
#     "clientSecret": Application Client Secret",
#     "clientScope": "Application Scope"
# }

username="$(cat authparam.json | jq -r .'username')"
password="$(cat authparam.json | jq -r .'password')"
clientId="$(cat authparam.json | jq -r .'clientId')"
clientSecret="$(cat authparam.json | jq -r .'clientSecret')"
clientScope="$(cat authparam.json | jq -r .'clientScope')"

auth_string="Basic $(echo -n ${clientId}:${clientSecret}|base64)"

curl -s --location \
--request POST 'https://nmdp.oktapreview.com/oauth2/ausaexcazhlhxknjs0h7/v1/token' \
--header 'Accept: application/json' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header "Authorization: ${auth_string}" \
--data-urlencode "grant_type=password" \
--data-urlencode "scope=${clientScope}" \
--data-urlencode "username=${username}" \
--data-urlencode "password=${password}" \
| jq -r '.access_token'