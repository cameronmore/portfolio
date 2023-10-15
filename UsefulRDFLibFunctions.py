from rdflib import Graph, Literal, URIRef
import re

g = Graph()

#Using Basic Formal Ontology as an example
graph =g.parse("BasicFormalOntology.ttl")


def get_elucidations():
    '''
    Returns a list of strings where the string contains the word 'elucidation'
    '''
    literals = [str(lit) for lit in g.objects() if isinstance(lit, Literal)]
    elucidations=[]
    for item in literals:
        match = re.search(r'\belucidation\b', item, re.IGNORECASE)
        if match is not None:
            elucidations.append(item)
            print(elucidations)

def get_definitions():
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


#Example Calls:
#replace_iri("http://www.w3.org/2000/01/rdf-schema#label","http://www.w3.org/2004/02/skos/core#prefLabel")
#g.serialize("bfo_label_replaced.ttl")
#get_definitions()
#get_elucidations



