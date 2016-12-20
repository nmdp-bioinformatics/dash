00_Patient 
    contains a simple example of an instance of a Patient
    resource.  POSTing this to a FHIR server will return the URI
    endpoint of the resource instance. For example, it might
    look like

    http://fhirtest.b12x.org/baseDstu3/Patient/27/_history/1

    Keep track of the URI if you want to reuse the same Patient with 
    another resource instance.

01_Specimen
    example of an instance of Specimen resource, that represents a buccal swab
    from the Patient described above.

02_SimpleTransactionBundle 
    A single transaction bundle that creates a Patient, a
    Specimen from that patient, a Sequence from that Speciment,
    and an Observation about a single HLA-A allele

03_HLA_ABC_scenario 
    This represents an HLA genotyping report of HLA-A, -B,
    and -C based on sequencing of exons 2 and 3.  This contains
    two transaction bundles. One to create resources ahead of 
    time that should be in the system ahead of time, such
    as Patient, Specimen, Organizations, and a DiagnosticRequest
    that was sent to the typing lab. The second bundle is the
    HLA typing report containing the DiagosticReport, and
    supporting Obervations and Sequences.

