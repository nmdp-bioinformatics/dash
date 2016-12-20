README.txt - Bob Milius - NMDP - 2016-12-19

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

FILES: 

+ 01Bundle_PatSpecOrgDiagRqst.xml
  - Transaction bundle used to pre-populate your FHIR server containing 
    Patient, Specimen, Organizations, and DiagnosticRequest. 
    The resulting URIs are used to populate the report bundle.
    
  - Files containing resource instances created by POSTing this bundle are 
    found in the created_resources subdirectory:

    Patient_402-MaryChalmers.xml
    Specimen_403_buccalswab.xml
    Organization_404-typinglab.xml
    Organization_405-registry.xml
    DiagnosticRequest_406-HLA_ABC.xml

+ 02BundleReport.xml
  - Transaction bundle containing the DiagnosticReport with 
    supporting Observations, and Sequences  

  - Files containing resource instances created by POSTing this bundle are
    found in the created_resources subdirectory:

    FILE                                     DESCRIPTION
    ----                                     -----------
    DiagnosticReport_428-HLA_ABC.xml       - Summary report  

    Observation_421-HLA_A.xml              - HLA-A            genotype
    Observation_419-HLA_A_01_01_01G.xml    - HLA-A*01:01:01G  allele assignment
    Observation_420-HLA_A_01_02.xml        - HLA-A*01:02      allele assignment
    Sequence_407-HLA_A_01_01_01G-ex2.xml   - HLA-A*01:01:01G  exon 2 sequence 
    Sequence_408-HLA_A_01_01_01G-ex3.xml   - HLA-A*01:01:01G  exon 3 sequence
    Sequence_409-HLA_A_01_02-ex2.xml       - HLA-A*01:02      exon 2 sequence
    Sequence_410-HLA_A_01_02-ex3.xml       - HLA-A*01:02      exon 3 sequence

    Observation_424-HLA_B.xml              - HLA-B            genotype
    Observation_422-HLA_B_15_01_01G.xml    - HLA-B*15:01:01G  allele assignment
    Observation_423-HLA_B_57_01_01G.xml    - HLA-B*57:01:01G  allele assignment
    Sequence_411-HLA_B_15_01_01G-ex2.xml   - HLA-B*15:01:01G  exon 2 sequence
    Sequence_412-HLA_B_15_01_01G-ex3.xml   - HLA-B*15:01:01G  exon 3 sequence
    Sequence_413-HLA_B_57_01_01G-ex2.xml   - HLA-B*57:01:01G  exon 2 sequence
    Sequence_414-HLA_B_57_01_01G-ex3.xml   - HLA-B*57:01:01G  exon 3 sequence

    Observation_427-HLA_C.xml              - HLA-C            genotype
    Observation_425-HLA_C_01_02_01G.xml    - HLA-C*01:02:01G  allele assignment
    Observation_426-HLA_C_03_04_01G.xml    - HLA-C*03:04:01G  allele assignment
    Sequence_415-HLA_C_01_02_01G-ex2.xml   - HLA-C*01:02:01G  exon 2 sequence
    Sequence_416-HLA_C_01_02_01G-ex3.xml   - HLA-C*01:02:01G  exon 3 sequence
    Sequence_417-HLA_C_03_04_01G-ex2.xml   - HLA-C*03:04:01G  exon 2 sequence
    Sequence_418-HLA_C_03_04_01G-ex3.xml   - HLA-C*03:04:01G  exon 3 sequence

