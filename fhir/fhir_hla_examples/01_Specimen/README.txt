Specimen.xml is an example of a simple Specimen resource instance that describes
a buccal swab collected from patient John Doe.
In this resource instance, the <subject> element points to the Patient resource
for John Doe, so that Patient resource must exist first. See the example in 
the 00_Patient directory.

This file (Specimen.xml) can be POSTed to a FHIR server. 

For example, to do this with the cURL command line tool:
curl -H "Content-Type: text/xml" -d @Specimen.xml  -X POST http://fhirtest.b12x.org/baseDstu3/Specimen

Also included are two code snippets demostrating how this can be with Python3. 
Both of these python programs POSTs a Patient resource instance to fhirtest.b12.org.
One has the Patient xml embedded in the python code. The other reads the Patient
data from an XML file.

Specimen1.py - XML read from Specimen.xml file
