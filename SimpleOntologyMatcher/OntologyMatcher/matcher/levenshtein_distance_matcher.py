'''
Created on 09.09.2016

@author: Philipp Schroeter
'''

import re
import util

#tries to match two ontologies just by comapring the labels of nodes
#returns a list, which holds information about nodes that are assumed to be linked on some way
# each item in the list has the following elements (in this order): IRI of the first element, it's label, the IRI of the second element, it's label, a string that states, why those elements have been chosen
def match_two_ontologies(results, onto, onto1):
    dist_calc = util.distance_calculator()
    #ensure that there are actually ontologies to compare
    if onto is not None and onto1 is not None:
        connections = {"matches":[], "text": "Matching by calculating the Levenshtein distances of the labels (levenshtein_distance_matcher)"}
        #go through all other ontologies
        #go through all elements
        print "Calculating Levenshtein distance for elements of ontologies " + onto.name + " and " + onto1.name
        onto_elements = onto.get_elements()
        onto1_elements = onto1.get_elements()
        for i in onto_elements:
            try:
                label = i.get_children_named("{http://www.w3.org/2000/01/rdf-schema#}label")
                if label != []:
                    for item in label:
                        for j in onto1_elements:
                            label1 = j.get_children_named("{http://www.w3.org/2000/01/rdf-schema#}label")
                            already_matched = False
                            if label1 != []:
                                for item1 in label1:
                                    if len(item.get_text()) > 3 and len(item1.get_text()) > 3:
                                        distance = dist_calc.calculate_distance(item.get_text().replace("_", " "), item1.get_text().replace("_", " "))
                                        #if the labels are not the same, but are similar, the nodes might be, too
                                        #version 1
                                        # if 1 < distance and distance < 5 and (distance < len(item.get_text())/3) and not already_matched:
                                        #version 2
                                        if not already_matched and 1 < distance and distance < 5 and (distance < len(item.get_text())/3) and (distance < len(item1.get_text())/3) and not re.match(i.name, j.name, re.IGNORECASE):
                                            #extra conditions, kept for testing
                                            # and label.get_text()[0] == label1.get_text()[0]
                                            connections["matches"].append([i.name, item.get_text(), j.name, item1.get_text(), " have the Levenshtein distance: " + str(distance)])
                                            already_matched = True
            except re.error:
                #just ignore errors during regular expression operations and try to go on
                pass
        return results.append(connections)