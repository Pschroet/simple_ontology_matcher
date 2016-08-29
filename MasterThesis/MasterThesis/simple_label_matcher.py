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
        print "Comparing ontologies " + onto.name + " and " + onto1.name
        onto_elements = onto.get_elements()
        onto1_elements = onto1.get_elements()
        for i in onto_elements:
            try:
                #util.write2File("regex.txt", i.name + ":" + "\n", "a")
                if i.get_child("{http://www.w3.org/2000/01/rdf-schema#}label") != None:
                    util.write2File("regex.txt", "-> " + i.get_child("{http://www.w3.org/2000/01/rdf-schema#}label").get_text() + "\n", "a")
                #if i.get_child("{http://www.w3.org/2000/01/rdf-schema#}comment") != None:
                #    util.write2File("regex.txt", "-> " + i.get_child("{http://www.w3.org/2000/01/rdf-schema#}comment").get_text() + "\n", "a")
                for j in onto1_elements:
                    label = i.get_child("{http://www.w3.org/2000/01/rdf-schema#}label")
                    label1 = i.get_child("{http://www.w3.org/2000/01/rdf-schema#}label")
                    if label != None and label1 != None:
                        match_result = re.match(label.get_text(), label1, re.IGNORECASE)
                        if match_result:
                            util.write2File("matching.txt", "Nodes " + i.name + " and " + j.name + " have the same label: " + label.get_text() + "\n", "a")
                    #comment = i.get_child("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}comment")
                    #if comment != None:
                    #    match_result = re.match(".*" + comment.get_text() + ".*", j.name, re.IGNORECASE)
                    #    if match_result:
                    #        util.write2File("matching.txt", "Nodes " + i.name + " and " + j.name + " are similar, because of the comment\n", "a")
            except re.error:
                #just ignore errors during regular expression operations and try to go on
                pass