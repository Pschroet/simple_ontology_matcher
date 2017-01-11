'''
Created on 11.01.2017

@author: Philipp Schroeter
'''
import json
import onto_element
import ontology
import os
import util

def parse_ontology_file(terminology_file):
    print "Parsing " + terminology_file
    #get the URI of the terminology and create a new instance of ontology
    json_content = util.readFileContentAsString(terminology_file)
    jo = json.loads(json_content)
    onto = ontology.ontology(os.path.basename(terminology_file))
    #get all terms of the termonology
    tempElems = []
    #get all terms and create them as instances of onto_elem
    for term in jo["results"]:
        elem = onto_element.onto_elem(term["uri"], "", "")
        elem.add_child(onto_element.onto_elem("{http://www.w3.org/2000/01/rdf-schema#}label",  "{http://www.w3.org/2000/01/rdf-schema#}label", term["label"]))
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