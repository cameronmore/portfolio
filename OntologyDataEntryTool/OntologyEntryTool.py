import rdflib
from rdflib import Graph
graph = rdflib.Graph()

g = Graph()
# Fetch the ontology from a URL
ontology_url = 'cardinality_test.ttl' # Change this to your ontology URL
graph.parse(ontology_url, format='turtle')

# Define the RDF and OWL terms
rdf = rdflib.Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
owl = rdflib.Namespace("http://www.w3.org/2002/07/owl#")

# Ask for the name of the instance and the class
InstName = input('Name of the instance: ')
ClsName = input('Name of the class: ')

# Find or create the URI of the instance and the class
InstURI = rdflib.URIRef(f'http://example.org/myOntology#{InstName}')
ClsURI = rdflib.URIRef(f'http://example.org/myOntology#{ClsName}')

# Add the instance to the class
g.add((InstURI, rdf.type, ClsURI))

# Query the graph for all the object properties that have the class as domain or range
q = """
    SELECT ?p WHERE {
        {?p rdf:type owl:ObjectProperty .
         ?p rdfs:domain ?c .
         FILTER (?c = %s)}
        UNION
        {?p rdf:type owl:ObjectProperty .
         ?p rdfs:range ?c .
         FILTER (?c = %s)}
    }
    """ % (ClsURI.n3(), ClsURI.n3())

# Execute the query and print the results
results = g.query(q)
print(results)
temporary_data=[]
for row in results:
    # Ask for the value of each object property for the instance
    value = input(f'Put in the value of {row.p} for {InstName}: ')
    # Add the triple to the graph
    new_trip=(InstURI, row.p, value)
    temporary_data.append(new_trip)
    print(temporary_data)

print(temporary_data)