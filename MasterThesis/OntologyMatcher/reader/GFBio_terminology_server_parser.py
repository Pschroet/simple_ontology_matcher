'''
Created on 01.10.2016

@author: Philipp Schroeter
'''

import json
import onto_element
import ontology
import requests

def parse_ontology_file(terminology):
    print "Parsing " + terminology
    #get the URI of the terminology and create a new instance of ontology
    re= requests.get(terminology)
    jo = json.loads(re.text)
    onto = ontology.ontology(terminology)
    #get all terms of the termonology
    re1= requests.get("http://terminologies.gfbio.org/api/terminologies/" + jo["results"][0]["acronym"] + "/allterms")
    jo1 = json.loads(re1.text)
    tempElems = []
    #get all terms and create them as instances of onto_elem
    for term in jo1["results"]:
        elem = onto_element.onto_elem(term["uri"], "", "")
        elem.add_child(onto_element.onto_elem("{http://www.w3.org/2000/01/rdf-schema#}label",  "{http://www.w3.org/2000/01/rdf-schema#}label", term["label"]))
        #get the synonyms
        re2= requests.get("http://terminologies.gfbio.org/api/terminologies/" + jo["results"][0]["acronym"] + "/synonyms?uri=" + term["uri"])
        jo2 = json.loads(re2.text)
        if "synonyms" in jo2["results"]:
            elem.add_attribute("synonyms", jo2["results"]["synonyms"])
        #save the term
        tempElems.append(elem)
        #print elem.tostring()
    if onto != "" and len(tempElems) > 0:
        onto.add_elements(tempElems)
    if onto != "":
        #util.write2File("onto.txt", str(onto) + os.linesep, "a")
        #util.write2File("onto.txt", str(onto.get_elements()) + os.linesep, "a")
        return onto
    else:
        return ""