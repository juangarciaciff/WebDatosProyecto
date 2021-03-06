"""
@author: U{Nines Sanguino}
@version: 0.2
@since: 20Jun2015
"""

__version__ = '0.2'
__modified__ = '20Jun2015'
__author__ = 'Nines Sanguino'
from SPARQLWrapper import SPARQLWrapper, JSON, XML, RDF
import xml.dom.minidom

####################################################################################################
### Obtiene una lista con todas las instancias que haya con sus label y lang
####################################################################################################
def getLocalLabel (instancia):
    print ">>> getLocalLabel"
    
    sparqlSesame = SPARQLWrapper("http://localhost:8080/openrdf-sesame/repositories/SocialNetwork",  returnFormat=JSON)
    queryString = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX sn:  <http://ciff.curso2015/ontologies/owl/socialNetwork#> SELECT ?label WHERE { sn:" + instancia + " rdfs:label ?label }"
    sparqlSesame.setQuery(queryString)
    sparqlSesame.setReturnFormat(JSON)
    query   = sparqlSesame.query()
    results = query.convert()
    devolver = []
    for result in results["results"]["bindings"]:
        label = result["label"]["value"]
        if 'xml:lang' in result["label"]:
            lang = result["label"]["xml:lang"]
        else:
            lang = None
        print "      - Label: " + label
        if 'xml:lang' in result["label"]:
            print "      - Lang.: " + lang
        devolver.append((label, lang))
    return devolver

####################################################################################################
### Obtiene informacion de DBPedia
####################################################################################################
def getDBpediaResource (label, lang, endpoint):
    print " "
    print ">>> getDBpediaResource"
    sparqlDBPedia = SPARQLWrapper(endpoint)
    if (lang):
        queryString = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX foaf: <http://xmlns.com/foaf/0.1/> SELECT ?s WHERE { ?s rdfs:label \"" + label + "\"@" +lang + " . ?s rdf:type foaf:Person} " 
    else:
        queryString = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX foaf: <http://xmlns.com/foaf/0.1/> SELECT ?s WHERE { ?s rdfs:label \"" + label + "\" . ?s rdf:type foaf:Person } " 
    sparqlDBPedia.setQuery(queryString)
    sparqlDBPedia.setReturnFormat(JSON)
    query   = sparqlDBPedia.query()
    results = query.convert()
    print "    * Resultados:"
    print results
    for result in results["results"]["bindings"]:
        resource = result["s"]["value"]
        print "      -> Resource: " + resource

####################################################################################################
### Obtiene informacion de Linkedmdb
####################################################################################################
def getLinkedmdbResource (label, lang, endpoint):
    print " "
    print ">>> getLinkedmdbResource"
    sparqlLinkedmdb = SPARQLWrapper(endpoint)
    if (lang):
        queryString = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX foaf: <http://xmlns.com/foaf/0.1/> PREFIX movie: <http://data.linkedmdb.org/resource/movie/> PREFIX lang: <http://www.lingvoj.org/lingvo/> SELECT ?resource WHERE {?resource rdfs:label \"" + label + "\"" ". ?resource movie:language lang:" + lang + " }"
    else:
        queryString = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX foaf: <http://xmlns.com/foaf/0.1/> PREFIX movie: <http://data.linkedmdb.org/resource/movie/> SELECT ?resource WHERE { ?resource rdfs:label \"" + label + "\"" "} "  
    sparqlLinkedmdb.setQuery(queryString)
    sparqlLinkedmdb.setReturnFormat(JSON)
    query   = sparqlLinkedmdb.query()
    results = query.convert()
    print "    * Resultados: "
    print results
    for result in results["results"]["bindings"]:
        resource = result["resource"]["value"]
        print "      -> Resource: " + resource

####################################################################################################
### Obtiene informacion de Webenemasuno
####################################################################################################
def getWebenemasunoResource (label, lang, endpoint):
    print " "
    print ">>> getWebenemasunoResource"
    sparqlWebenemasuno = SPARQLWrapper(endpoint)
    if (lang):
        queryString = "PREFIX sioc:<http://rdfs.org/sioc/ns#> PREFIX opmopviajero:<http://webenemasuno.linkeddata.es/ontology/OPMO/> SELECT ?resource WHERE {?resource sioc:title \"" + label + "\"" ". ?resource opmopviajero:language \"" + lang + "\"} "  
    else:
        queryString = "PREFIX sioc:<http://rdfs.org/sioc/ns#> PREFIX opmopviajero:<http://webenemasuno.linkeddata.es/ontology/OPMO/> SELECT ?resource WHERE {?resource sioc:title \"" + label + "\"} "
    sparqlWebenemasuno.setQuery(queryString)
    sparqlWebenemasuno.setReturnFormat(JSON)
    query   = sparqlWebenemasuno.query()
    results = query.convert()
    print "    * Resultados: "
    print results
    for result in results["results"]["bindings"]:
        resource = result["resource"]["value"]
        print "      ->The resource: " + resource

####################################################################################################
### Main
####################################################################################################
if __name__ == '__main__':

    # getLocalLabel devuelve una lista con todas las instancias que haya con sus label y lang
    # y luego se hace la llamada al repositorio externo para enriquecer cada combinacion de label-lang recibida
    print "\n================================================"
    print "=== Busqueda de informacion para la instancia 1"
    print "================================================\n"
    lista = getLocalLabel("instancia1");
    print "\n    * Resultados:"
    print lista
    endpoint = 'http://dbpedia.org/sparql';
    for result in lista:
        (label, lang) = result
        resource = getDBpediaResource (label, lang, endpoint);

    print "\n================================================"
    print "=== Busqueda de informacion para la instancia 3"
    print "================================================\n"
    lista = getLocalLabel("instancia3");
    print "\n    * Resultados:"
    print lista
    endpoint = 'http://data.linkedmdb.org/sparql';
    for result in lista:
        (label, lang) = result
        resource = getLinkedmdbResource (label, lang, endpoint);

    print "\n================================================"
    print "=== Busqueda de informacion para la instancia 4"
    print "================================================\n"
    lista = getLocalLabel("instancia4");
    print "\n    * Resultados:"
    print lista
    endpoint = 'http://webenemasuno.linkeddata.es/sparql';
    for result in lista:
        (label, lang) = result
        resource = getWebenemasunoResource (label, lang, endpoint);

