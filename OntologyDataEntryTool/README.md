## Ontology Data Entry Tool
This is a tool I'm currently working on that takes an ontology as input and dynamically prompts a user to input instances. More that that, it asks for the necessary object properties associated with each class. I created a small sample ontology to test the tools on, which I have called 'cardinality_tet.ttl'.
During my initial approach, I tried to have the script read the cardinality prompts and ask the user to input necessary object properties according to the cardinality restrictions, but I'm now trying to prompt the usr according to domain and range, using a SPARQL query.
This is a work in progress, so stay tuned and feel free to contribute.
