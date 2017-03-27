<img src="https://cloud.githubusercontent.com/assets/8644904/24367035/c3233d14-12e0-11e7-8251-6fcf81a64e56.png" alt="DaSH 5 CHORI" />

#History:
Four DaSH events have been held, in Bethesda, La Jolla, Minneapolis and Vienna.<br />


#What:
7 primary focus areas

1.	Prepare “feature service” for production use
•	Implement a versioning system for the feature service
•	Add authentication and security layers
•	Add curation capability linking sequences to 
o	IPD-KIR and IMGT/HLA Database accession release version and Accession number (a more accurate way of saying the allele name) 
o	the sequence submitter and their “de-novo” identifiers for sequences they have submitted, associated with a given GFE notation/set of locus/feature/rank/accession coordinates
•	Populate feature service with all versions of HLA.xml and KIR.dat
•	Improve documentation; make sure that the documentation is sufficient to inform an API for analytics; expand on the BTOP-like pairwise difference annotation

2.	GFE service enhancements 
•	Experiment with AWS configurations
•	Add a database cache
•	Volume test
•	Test installation process
•	Add clients and tools
•	Rename (service-gfe-submission -> service-gfe)
•	Connect to feature service with authentication

3.	GFE Service validation
•	Validation of alignments using “features” from HLA.xml and KIR.dat files
•	Develop automated tests; possibly using Neo4j

4.	Improve current capabilities of the annotation pipeline (within GFE service)
•	Make it a maven project; push code to maven central
•	Allow GFE service to utilize different version of annotation
•	Add capability of running ABO

5.	Haplotype Frequency Curation Service (HFCu) development
•	Build the shell of the backend based on the population service and check the code into GitHub 

6.	HL7 FHIR
Develop use cases:
•	Vendor perspective (create partially filled FHIR template)
o	identify what vendor software can pre-fill
o	e.g. sequence info, allele-assignments, sample identification, methodology
•	Lab perspective
o	fill in the rest of the data not available to vendor software
•	Transplant Center perspective
o	patient demographics, from EMR
•	Registry perspective
o	receive, process and verify bundle
Identify required resources for use case
Map data to resources
•	From HML
o	build bundle
o	POST to FHIR server
Create client that will search, GET and link resources from FHIR server.
Create a client that will access HLA terminology server.

7.	Integrate Chipper algorithm for predicting proteasome cleavage sites 
•	Add to peptide prediction pipeline(s) https://github.com/massie/chipper

# When: 
The meeting will start with an informal event on Sunday night, March 26th. We will work from 8:00 am on Friday 4th, finishing at 4:00 pm on Monday 27th March 2017, stopping when appropriate to eat and drink and socialize.

# Where:
In the Library at CHORI.

# Further details:
Please contact Michael Wright, mwright@nmdp.org

As the name 'hackathon' implies, the meeting is geared to 'implementers,' and less so to 'talkers' and 'directors.' 
