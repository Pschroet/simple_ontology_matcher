'''
Created on 13.09.2016

@author: Philipp Schroeter
'''

import collections
import imp
import logging
import os
import PyDictionary
import re
import util

#tries to match two ontologies just by comapring the labels of nodes
#returns a list, which holds information about nodes that are assumed to be linked on some way
# each item in the list has the following elements (in this order): IRI of the first element, it's label, the IRI of the second element, it's label, a string that states, why those elements have been chosen
def match_two_ontologies(onto, onto1):
    dictionary = PyDictionary.PyDictionary()
    #ensure that there are actually ontologies to compare
    if onto is not None and onto1 is not None:
        connections = {"matches":[], "text": "Synonyms"}
        #go through all other ontologies
        #go through all elements
        print "Searching for synonyms for elements of ontologies " + onto.name + " and " + onto1.name
        onto_elements = onto.get_elements()
        onto1_elements = onto1.get_elements()
        for i in onto_elements:
            try:
                label = i.get_children_named("{http://www.w3.org/2000/01/rdf-schema#}label")
                already_matched = False
                if label != []:
                    for item in label:
                        synonyms = dictionary.synonym(item.get_text().encode('utf8'))
                        print synonyms
                        #check if there is a list of synonyms and not None or a message
                        if synonyms is not None and hasattr(synonyms, '__getitem__') and hasattr(synonyms, '__iter__'):
                            for j in onto1_elements:
                                label1 = j.get_children_named("{http://www.w3.org/2000/01/rdf-schema#}label")
                                if label1 != []:
                                    for item1 in label1:
                                        #if the labels are not the same, but are similar, the nodes might be, too
                                        if item1.get_text() in synonyms and not already_matched:
                                            connections["matches"].append([i.name, "(" + item.get_text() + ")", j.name, "(" + item1.get_text() + ")", " are synonyms"])
                                            already_matched = True
            except re.error:
                #just ignore errors during regular expression operations and try to go on
                pass
        return connections