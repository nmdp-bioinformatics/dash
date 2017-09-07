<img src="https://raw.githubusercontent.com/nmdp-bioinformatics/dash/master/dashihiws.png">alt="DaSH IHIWS" />
# DaSH IHIWS
You are invited to participate in a data standards hackathon which will take place during the 17th workshop in the “Fred Farr Forum” room.  Thursday, Friday and Saturday Sept 7th-9th 9am-9pm

## Topics:
* Whole Gene HLA and KIR Analysis.  Automated annotation Gene Feature Enumeration.
* HL7-FHIR: Exchanging HLA and KIR NGS results using Health Level 7 Fast Healthcare Interoperability Resources (FHIR) for Clinical Genomics
* Tools for Allele and Haplotype Frequency Analysis of HLA and KIR

All attendees need to be registered for the IHIWS, but no further registration is required. 
Further details:  Please contact Martin Maiers, mmaiers@nmdp.org


## History:
Six Data Standards Hackathons (DaSH events) have been held since Fall 2014. These events are designed for groups of interested people to come together and produce open source software (hack) or decisions that will facilitate the analysis and interchange of HLA and KIR data. 

#Previous output:
1.	Minimum information for reporting next generation sequence genotyping (MIRING): Guidelines for reporting HLA and KIR genotyping via next generation sequencing 
Human Immmunology, doi:10.1016/j.humimm.2015.09.011 
2.	Histoimmunogenetics Markup Language 1.0: Reporting Next Generation Sequencing-based HLA and KIR Genotyping, 
Human Immmunology, doi:10.1016/j.humimm.2015.08.001 
3.	A gene feature enumeration approach for describing HLA allele polymorphism 
Human Immunology, doi:10.1016/j.humimm.2015.09.016
4.	https://github.com/nmdp-bioinformatics/dash/wiki 






<img src="https://cloud.githubusercontent.com/assets/8644904/24367035/c3233d14-12e0-11e7-8251-6fcf81a64e56.png" alt="DaSH 5 CHORI" />

#History:
6 DaSH events have been held, in Bethesda, La Jolla, Minneapolis and Vienna.<br />


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
