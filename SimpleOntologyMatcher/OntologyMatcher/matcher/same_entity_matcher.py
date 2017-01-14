'''
Created on 04.04.2017

@author: Philipp Schroeter
'''

import re
import util

#tries to match two ontologies just by comapring the labels of nodes
#returns a list, which holds information about nodes that are assumed to be linked on some way
# each item in the list has the following elements (in this order): IRI of the first element, it's label, the IRI of the second element, it's label, a string that states, why those elements have been chosen
def match_two_ontologies(results, onto, onto1):
    #ensure that there are actually ontologies to compare
    if onto is not None and onto1 is not None:
        #the current ontology, which is compared to the other ones
        connections = {"matches":[], "text":"Have the same URI, i.e. are the same entity"}
        #go through all other ontologies
        #go through all elements
        print "Comparing ontologies " + onto.name + " and " + onto1.name
        onto_elements = onto.get_elements()
        onto1_elements = onto1.get_elements()
        for i in onto_elements:
            for j in onto1_elements:
                if re.match(i.name, j.name, re.IGNORECASE):
                    i_label = i.get_child("{http://www.w3.org/2000/01/rdf-schema#}label")
                    if i_label is None:
                        i_label = ""
                    j_label = j.get_child("{http://www.w3.org/2000/01/rdf-schema#}label")
                    if j_label is None:
                        j_label = ""
                    connections["matches"].append([i.name, i_label.get_text(), j.name, j_label.get_text(), " have the same URI\n"])
        return results.append(connections)