Patient.xml is an example of a simple Patient resource, John Doe.
This file (Patient.xml) can be POSTed to a FHIR server. 

For example, to do this with the cURL command line tool:
curl -H "Content-Type: text/xml" -d @Patient.xml  -X POST http://fhirtest.b12x.org/baseDstu3/Patient

Also included are two code snippets demostrating how this can be with Python3. 
Both of these python programs POSTs a Patient resource instance to fhirtest.b12.org.
One has the Patient xml embedded in the python code. The other reads the Patient
data from an XML file.

Patient0.py - XML hard coded into the python code. 
Patient1.py - XML read from Patient.xml file
