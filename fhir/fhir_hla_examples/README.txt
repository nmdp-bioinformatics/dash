00_Patient 
    contains a simple example of an instance of a Patient resource. 
    POSTing this to a FHIR server will return the URI endpoint of the resource 
    instance. For example, it might look like

    http://fhirtest.b12x.org/baseDstu3/Patient/27/_history/1

    Keep track of the URI if you want to reuse the same Patient with another resource instance.

01_Specimen
    example of an instance of Specimen resource, that represents a buccal swab
    from the Patient described above.

02_SimpleTransactionBundle -
    A single transaction bundle that creates a Patient, a Specimen from that
    patient, a Sequence from that Speciment, and an Observation about a single
    HLA-A allele

