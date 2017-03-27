README.txt - Bob Milius - NMDP - 2017-03-27

This distribution contains HL7 FHIR resource instances used in a scenario for
reporting HLA typing data of a potential stem cell donor. This is a
proof-of-concept example and contains fictitious data. This example only shows
a simple example of typing of Class I genes. An example for both Class I and II
HLA genes will be presented in the future.

In this scenario, a donor registry (Organization) collected a buccal swab
(Specimen) from a potential stem cell donor (Patient). A lab order
(DiagnosticRequest) for HLA class I typing of HLA-A, -B, and -C was sent to the
a typing lab (Organization). The typing was done by sequencing exons 2 and 3 of
each gene. The results were uploaded as a transaction bundle consisting of the
final report (DiagnosticReport) and the supporting information including the
evidence leading to genotyping for each gene (Observations), identification of
separate alleles (Observations), and sequencing data for each exon (Sequences).
Because only exons 2 and 3 are sequenced, G-group level reporting done is for
most of the results with one exception which is not represented in a G-Group
(HLA-A:01:02).

This represents the information that are uploaded in two separate transaction
bundles in the 03_HLA_ABC_scenario directory, but combined in one bundle for
convenience to explore working with FHIR servers (transaction bundles) and 
clinFHIR (collection bundles). Both xml and json versions are provided.

These bundles conform to STU3.

Collection Bundles that may be uploaded to clinFHIR.com
- FullBundleCollection_HLA.json
- FullBundleCollection_HLA.xml

Transaction Bundles that may be POSTed to a FHIR server
- FullBundleTransaction_HLA.json
- FullBundleTransaction_HLA.xml
