Bob Milius - NMDP - 2016-05-09

Transaction bundle that creates and links:
+ Patient

+ Specimen from that Patient, which was collected as a buccal swab
    - points to Patient

+ Sequence from that Specimen
	- single sequence
	- uses HLA-A*01:01:01:01 from IPD-IMGT/HLA as reference 
    - G->T substitution at position 5 (I made this up)
    - points to Patient and Specimen

+ Observation with genomics extensions that includes
    - LOINC for HLA-A high resolution,
    - targeting the HLA-A gene,
    - source is "germline"
    - resulting in a single allele assignment HLA-A:01:01:01:01, even though there is novel variation!!
	- points to Patient, Sample, and Sequence

You can POST this file to the FHIR development server using a number of 
different clients such as the POSTMAN Google Chrome plugin, in your code, or 
a command line tool such as Curl. Here's an example of sending this file to
the development FHIR server hosted by NMDP:

curl -H "Content-Type: text/xml" -d @Transaction01.xml -X POST http://fhirtest.b12x.org/baseDstu3

and it should return something similar to this, but with different ids, timestamps, 
and endpoint URIs for the individual resources created.

<Bundle xmlns="http://hl7.org/fhir">
   <id value="9ec0fe08-46d5-4e99-b3fb-c72f541eb3c6"/>
   <type value="transaction-response"/>
   <link>
      <relation value="self"/>
      <url value="http://fhirtest.b12x.org/baseDstu3"/>
   </link>
   <entry>
      <response>
         <status value="201 Created"/>
         <location value="Patient/21/_history/1"/>
         <etag value="1"/>
         <lastModified value="2016-11-02T20:25:21.895+00:00"/>
      </response>
   </entry>
   <entry>
      <response>
         <status value="201 Created"/>
         <location value="Specimen/22/_history/1"/>
         <etag value="1"/>
         <lastModified value="2016-11-02T20:25:21.906+00:00"/>
      </response>
   </entry>
   <entry>
      <response>
         <status value="201 Created"/>
         <location value="Sequence/23/_history/1"/>
         <etag value="1"/>
         <lastModified value="2016-11-02T20:25:21.909+00:00"/>
      </response>
   </entry>
   <entry>
      <response>
         <status value="201 Created"/>
         <location value="Observation/24/_history/1"/>
         <etag value="1"/>
         <lastModified value="2016-11-02T20:25:21.915+00:00"/>
      </response>
   </entry>
</Bundle>
