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

import json

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
        queryString = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX foaf: <http://xmlns.com/foaf/0.1/> PREFIX dbo: <http://dbpedia.org/ontology/> SELECT ?s ?birthDate ?birthPlace ?birthName ?abstract WHERE { ?s dbo:birthDate ?birthDate . ?s dbo:birthPlace ?birthPlace . ?s dbo:birthName ?birthName . ?s dbo:abstract ?abstract . ?s rdfs:label \"" + label + "\"@" +lang + " . ?s rdf:type foaf:Person }"; 
    else:
        queryString = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX foaf: <http://xmlns.com/foaf/0.1/> PREFIX dbo: <http://dbpedia.org/ontology/> SELECT ?s ?birthDate ?birthPlace ?birthName ?abstract WHERE { ?s dbo:birthDate ?birthDate . ?s dbo:birthPlace ?birthPlace . ?s dbo:birthName ?birthName . ?s dbo:abstract ?abstract . ?s rdfs:label \"" + label + " . ?s rdf:type foaf:Person }"; 
    sparqlDBPedia.setQuery(queryString)
    sparqlDBPedia.setReturnFormat(JSON)
    query   = sparqlDBPedia.query()
    results = query.convert()
    with open('/home/wod/instancia1.json', 'w') as outfile:
        json.dump(results, outfile, indent=4, sort_keys=True, separators=(',', ':')) 
    print "    * Resultados:"
    print results
    for result in results["results"]["bindings"]:
        resource = result["s"]["value"]
        abstract = result["abstract"]["value"]
        birthDate = result["birthDate"]["value"]
        birthPlace = result["birthPlace"]["value"]
        birthName = result["birthName"]["value"]
        print "      -> Resource: " + resource
        print "      -> birthDate: " + birthDate
        print "      -> birthPlace: " + birthPlace
        print "      -> birthName: " + birthName

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
        queryString = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX foaf: <http://xmlns.com/foaf/0.1/> PREFIX movie: <http://data.linkedmdb.org/resource/movie/> PREFIX lang: <http://www.lingvoj.org/lingvo/> SELECT ?resource WHERE {?resource rdfs:label \"" + label + "\"" "} "  
    sparqlLinkedmdb.setQuery(queryString)
    sparqlLinkedmdb.setReturnFormat(JSON)
    query   = sparqlLinkedmdb.query()
    results = query.convert()
    with open('/home/wod/instancia3.json', 'w') as outfile:
        json.dump(results, outfile, indent=4, sort_keys=True, separators=(',', ':')) 
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
        queryString = "PREFIX sioc:<http://rdfs.org/sioc/ns#> PREFIX opmopviajero:<http://webenemasuno.linkeddata.es/ontology/OPMO/> PREFIX opmo:<http://openprovenance.org/model/opmo#> SELECT  ?title ?created_at ?has_creator ?content ?language WHERE { ?s sioc:title ?title. ?s sioc:created_at ?created_at. ?s sioc:has_creator ?has_creator. ?s opmo:content ?content. ?s opmopviajero:language ?language. ?s sioc:title \"" + label + "\"" ". ?s opmopviajero:language \"" + lang + "\"} "  
    else:
        queryString = "PREFIX sioc:<http://rdfs.org/sioc/ns#> PREFIX opmopviajero:<http://webenemasuno.linkeddata.es/ontology/OPMO/> PREFIX opmo:<http://openprovenance.org/model/opmo#> SELECT  ?title ?created_at ?has_creator ?content ?language WHERE { ?s sioc:title ?title. ?s sioc:created_at ?created_at. ?s sioc:has_creator ?has_creator. ?s opmo:content ?content. ?s opmopviajero:language ?language. ?s sioc:title \"" + label + "\"} "
    sparqlWebenemasuno.setQuery(queryString)
    sparqlWebenemasuno.setReturnFormat(JSON)
    query   = sparqlWebenemasuno.query()
    results = query.convert()
    with open('/home/wod/instancia4.json', 'w') as outfile:
        json.dump(results, outfile, indent=4, sort_keys=True, separators=(',', ':')) 
    print "    * Resultados: "
    print results
    for result in results["results"]["bindings"]:
        title = result["title"]["value"]
        created_at = result["created_at"]["value"]
        language = result["language"]["value"]
        content = result["content"]["value"]
        print "      ->Title: " + title
        print "      ->Created at: " + created_at
        print "      ->Language: " + language

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

