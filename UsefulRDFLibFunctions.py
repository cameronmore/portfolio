from rdflib import Graph, Literal, URIRef
import re

g = Graph()

#Using Basic Formal Ontology as an example
graph =g.parse("BasicFormalOntology.ttl")


def get_elucidations() -> list:
    '''
    Returns a list of strings where the string contains the word 'elucidation'. Note, this will return labels with the word 'elucidation'
    '''
    literals = [str(lit) for lit in g.objects() if isinstance(lit, Literal)]
    elucidations=[]
    for item in literals:
        match = re.search(r'\belucidation\b', item, re.IGNORECASE)
        if match is not None:
            elucidations.append(item)
            print(elucidations)

def get_definitions() -> list:
    '''
    Returns a list of strings where the string is the value of cco:definition or skos:definition
    '''
    query="""
    PREFIX obo: <http://purl.obolibrary.org/obo/>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX cco: <http://www.ontologyrepository.com/CommonCoreOntologies/>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    SELECT ?definition
    WHERE {
        ?s cco:definition|skos:definition ?definition .
        }
        """
    results = g.query(query)
    for row in results:
        definitions = [str(row[0]) for row in results]
        print(definitions)

def replace_iri(old_iri: str, new_iri: str) -> Graph:
    '''
    Returns a graph with the iri replaced, stored in memory, not serialized. Note, takes full iri string, no prefixes.
    '''
    old_iri = URIRef(old_iri)
    new_iri = URIRef(new_iri)
    
    for s, p, o in graph.triples((None, None, None)):
        if s == old_iri:
            graph.remove((s, p, o))
            graph.add((new_iri, p, o))
        if p == old_iri:
            graph.remove((s, p, o))
            graph.add((s, new_iri, o))
        if o == old_iri:
            graph.remove((s, p, o))
            graph.add((s, p, new_iri))
    return graph


def check_if_label_matches_iri() -> list:
    """
    Relies on the Python module 're' so make sure 'import re' is asserted.    
    Checks if the rdfs:label for a class is the same as the end of the IRI.
    This function parses whatever ontology is already parsed in graph = g.parse("YOUR_ONTOLOGY.ttl") .
    """
    #Define the query
    q ="""
    SELECT ?c ?d
    WHERE { 
    ?c rdf:type owl:Class ;
        rdfs:label ?d .
        FILTER (!isBlank(?c)) 
    }"""
    #Execute the query
    qres = g.query(q)
    unnormalized_iris = []
    for row in qres:
        full_iri = row[0]
        label_string = (str(row[1])).replace(" ","")
        normalized_label_string = (re.sub("[^a-zA-Z]+", "", label_string)).upper()
        label_length=len(label_string)
        full_iri_as_string = str(row[0])
        end_of_iri = full_iri_as_string[-int(label_length):]
        normalized_end_of_iri = (re.sub("[^a-zA-Z]+", "", end_of_iri)).upper()
        if normalized_end_of_iri != normalized_label_string:
            unnormalized_iris.append(full_iri_as_string)
    print(unnormalized_iris)





#Example Calls:
#check_if_label_matches_iri()
#replace_iri("http://www.w3.org/2000/01/rdf-schema#label","http://www.w3.org/2004/02/skos/core#prefLabel")
#g.serialize("bfo_label_replaced.ttl")
#get_definitions()
#get_elucidations



