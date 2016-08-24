'''
Created on 23.08.2016

@author: Philipp Schroeter
'''
import ontology
import os
import re
import string
import time
import util

#tries to match two ontologies just by comapring the labels of nodes
#returns a bridge ontology, which holds information about nodes that are assumed to be linked on some way
def match_two_ontologies(onto, onto1):
    #remove content of debug file 'matching.txt'
    util.write2File("matching.txt", "", "w")
    if onto is not None and onto1 is not None:
        #the current ontology, which is compared to the other ones
        bridge_ontology = ontology.ontology("bridge-" + str(time.localtime()))
        #go through all other ontologies
        #go through all elements
        onto_elements = onto.get_elements()
        onto1_elements = onto1.get_elements()
        #print onto_elements
        #print onto1_elements
        print "Going through ontology " + onto.name
        for i in onto_elements:
            try:
                for j in onto1_elements:
                    labels = i.get_children_named("{http://www.w3.org/2000/01/rdf-schema#}label")
                    for label in labels:
                        labelChildren = j.get_children_named("{http://www.w3.org/2000/01/rdf-schema#}label")
                        if(len(labelChildren) > 0) and label.get_attribute("{http://www.w3.org/XML/1998/namespace}lang") == "en" and string.upper(label.get_text()) == string.upper(labelChildren[0].get_text()):
                            util.write2File("matching.txt", "Nodes " + i.name + " (Label: " + label.get_text() + ") and " + j.name + " (Label: " + j.get_children_named("{http://www.w3.org/2000/01/rdf-schema#}label")[0].get_text() + ")" + " have the exact same label" + "\n", "a")
                #for j in onto1_elements:
                #    labels = i.get_children_named("{http://www.w3.org/2000/01/rdf-schema#}label")
                #    for label in labels:
                #        match_result = re.match(label.get_text(), j.get_children_named("{http://www.w3.org/2000/01/rdf-schema#}label")[0].get_text(), re.IGNORECASE)
                #        if match_result:
                #            util.write2File("matching.txt", "Nodes " + i.name + " (Label: " + label.get_text() + ") and " + j.name + " (Label: " + j.get_children_named("{http://www.w3.org/2000/01/rdf-schema#}label")[0].get_text() + ")" + " are similar, because of the label" + "\n", "a")
                    #comment = i.get_child("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}comment")
                    #if comment != None:
                    #    match_result = re.match(".*" + j.name.replace("http://purl.obolibrary.org/obo/", "") + ".*", comment.get_text(), re.IGNORECASE)
                    #    if match_result:
                    #        util.write2File("matching.txt", "Nodes " + i.name + " and " + j.name + " are similar, because of the comment\n", "a")
            except re.error:
                pass