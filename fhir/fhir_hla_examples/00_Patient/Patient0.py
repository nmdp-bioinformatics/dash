import requests
url = 'http://fhirtest.b12x.org/baseDstu3/Patient'
headers = {'content-type': 'text/xml'}
xml = """<Patient>
    <text>
        <div>Some narrative</div>
    </text>
    <name>
        <use value="official"/>
        <family value="Doe"/>
        <given value="John"/>
    </name>
    <gender value="male"/>
    <birthDate value="1974-12-25"/>
</Patient>"""
#print(xml)
r = requests.post(url, data=xml, headers=headers)
print('URL =', r.url, end='\n\n')
print('text =', r.text, end='\n\n')
print('response headers =', r.headers, end='\n\n')
