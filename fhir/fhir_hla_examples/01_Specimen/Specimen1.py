import requests
url = 'http://fhirtest.b12x.org/baseDstu3/Specimen'
headers = {'content-type': 'text/xml'}
with open("Specimen.xml", "r") as myfile:
    xml=myfile.read()
#print(xml)
r = requests.post(url, data=xml, headers=headers)
print('URL =', r.url, end='\n\n')
print('text =', r.text, end='\n\n')
print('response headers =', r.headers, end='\n\n')

