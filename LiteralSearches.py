from rdflib import Graph, Literal
import re

g = Graph()

#Your ontology goes here
g.parse("BasicFormalOntology.ttl")


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

