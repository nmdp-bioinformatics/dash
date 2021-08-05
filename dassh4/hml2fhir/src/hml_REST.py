import sys
import requests

if len(sys.argv) < 2:
    sys.exit("Usage: python hml_REST.py <hml_file_name>")
    
url = 'https://qa-api.nmdp.org/hml_gw/v1/submit'
access_token = ''


hml_params = {'testSubmit':'false'}

hml_headers = {
    'Authorization' : 'Bearer ' + access_token, 
    'Connection' : 'close', 
    'Content-Type' : 'application/xml', 
    'cache-control' : 'no_cache'
}

with open(sys.argv[1], 'r') as f2:
    hml_file = f2.read()

s = requests.session()

response = s.post(url, data=hml_file, headers=hml_headers, params=hml_params)

print(response.text)
