'''
Created on 09.09.2016

@author: Philipp Schroeter
'''

import imp
import logging
import ontology
import os
import re
import time
import util

#tries to match two ontologies just by comapring the labels of nodes
#returns a bridge ontology, which holds information about nodes that are assumed to be linked on some way
def match_two_ontologies(onto, onto1):
    dist_calc = util.distance_calculator()
    #ensure that there are actually ontologies to compare
    if onto is not None and onto1 is not None:
        #the current ontology, which is compared to the other ones
        #bridge_ontology = ontology.ontology("bridge-" + str(time.localtime()))
        connections = {"matches":[], "text": "Levenshtein Distances (1 < distance < 5)"}
        #go through all other ontologies
        #go through all elements
        print "Calculating Levenshtein distance for elements of ontologies " + onto.name + " and " + onto1.name
        onto_elements = onto.get_elements()
        onto1_elements = onto1.get_elements()
        for i in onto_elements:
            try:
                label = i.get_child("{http://www.w3.org/2000/01/rdf-schema#}label")
                if label != None:
                    for j in onto1_elements:
                        label1 = j.get_child("{http://www.w3.org/2000/01/rdf-schema#}label")
                        if label1 != None and len(label.get_text()) > 3 and len(label1.get_text()) > 3:
                            distance = dist_calc.calculate_distance(label.get_text(), label1.get_text())
                            #if the labels are not the same, but are similar, the nodes might be, too
                            if 1 < distance and distance < 5 and (distance < len(label.get_text())/3 and distance < len(label1.get_text())/3):
                                #extra conditions, kept for testing
                                # and label.get_text()[0] == label1.get_text()[0]
                                #util.write2File("matching.txt", "Nodes " + i.name + "(" + label.get_text() + ")" + " and " + j.name + "(" + label1.get_text() + ")" + " have the Levenshtein distance: " + str(distance) + "\n", "a")
                                connections["matches"].append([i.name, "(" + label.get_text() + ")", j.name, "(" + label1.get_text() + ")", " have the Levenshtein distance: " + str(distance)])
            except re.error:
                #just ignore errors during regular expression operations and try to go on
                pass
        return connections