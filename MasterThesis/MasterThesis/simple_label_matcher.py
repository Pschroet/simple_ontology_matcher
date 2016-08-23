'''
Created on 19.08.2016

@author: Philipp Schroeter
'''

import ontology
import os
import re
import time
import util

#tries to match two ontologies just by comapring the labels of nodes
#returns a bridge ontology, which holds information about nodes that are assumed to be linked on some way
def match_two_ontologies(onto, onto1):
    if onto is not None and onto1 is not None:
        #the current ontology, which is compared to the other ones
        bridge_ontology = ontology.ontology("bridge-" + str(time.localtime()))
        #go through all other ontologies
        #go through all elements
        print "Going through ontology " + onto.name
        onto_elements = onto.get_elements()
        onto1_elements = onto1.get_elements()
        #print onto_elements
        #print onto1_elements
        for i in onto_elements:
            try:
                util.write2File("regex.txt", i.name + ": " + i.get_child("{http://www.w3.org/2000/01/rdf-schema#}label").get_text() + "\n", "a")
                for j in onto1_elements:
                    match_result = re.match(".*" + i.get_child("{http://www.w3.org/2000/01/rdf-schema#}label").get_text() + ".*", j.name)
                    if match_result:
                        util.write2File("matching.txt", "Nodes " + i.name + " and " + j.name + " are similar\n", "a")
            except re.error:
                pass
        print "Going through ontology " + onto1.name
        for k in onto1_elements:
            try:
                util.write2File("regex.txt", k.name + ": " + k.get_child("{http://www.w3.org/2000/01/rdf-schema#}label").get_text() + "\n", "a")
                for l in onto_elements:
                    match_result1 = re.match(".*" + k.get_child("{http://www.w3.org/2000/01/rdf-schema#}label").get_text() + ".*", l.name)
                    if match_result1:
                        util.write2File("matching.txt", "Nodes " + k.name + " and " + l.name + " are similar\n", "a")
            except re.error:
                pass