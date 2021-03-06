'''
Created on 19.08.2016

@author: Philipp Schroeter
'''

import re
import util

#tries to match two ontologies just by comapring the labels of nodes
#returns a list, which holds information about nodes that are assumed to be linked on some way
# each item in the list has the following elements (in this order): IRI of the first element, it's label, the IRI of the second element, it's label, a string that states, why those elements have been chosen
def match_two_ontologies(results, onto, onto1, exact_match = False):
    #ensure that there are actually ontologies to compare
    if onto is not None and onto1 is not None:
        #the current ontology, which is compared to the other ones
        connections = {"matches":[], "text":"Matching by lexical analysis of the labels (simple_label_matcher)"}
        #go through all other ontologies
        #go through all elements
        print "Comparing ontologies " + onto.name + " and " + onto1.name
        onto_elements = onto.get_elements()
        onto1_elements = onto1.get_elements()
        for i in onto_elements:
            try:
                label = i.get_children_named("{http://www.w3.org/2000/01/rdf-schema#}label")
                if label != []:
                    for item in label:
                        for j in onto1_elements:
                            label1 = j.get_children_named("{http://www.w3.org/2000/01/rdf-schema#}label")
                            if label1 != []:
                                for item1 in label1:
                                    already_matched = False
                                    match_result = re.match("^" + item.get_text().replace("_", " ") + "$", item1.get_text().replace("_", " "), re.IGNORECASE)
                                    if not already_matched and match_result and not re.match(i.name, j.name, re.IGNORECASE):
                                        #util.write2File("matching.txt", "Nodes " + i.name + " (" + label.get_text() + ")" + " and " + j.name + " (" + label1.get_text() + ")" + " have the same label\n", "a")
                                        connections["matches"].append([i.name, item.get_text(), j.name, item1.get_text(), " have the same label\n", "owl:sameAs"])
                                        already_matched = True
                                    #if the labels don't match already, check if the expression of the labels is at the beginning or end of the other
                                    elif not exact_match and not already_matched and len(item.get_text()) > 3 and len(item1.get_text()) > 3 and not re.match(i.name, j.name, re.IGNORECASE):
                                        #check the first of the two labels
                                        if re.match("^" + item.get_text().replace("_", " ") + "\s", item1.get_text().replace("_", " "), re.IGNORECASE):
                                            connections["matches"].append([i.name, item.get_text(), j.name, item1.get_text(), " share part of the label\n", "dcterms:hasPart"])
                                            already_matched = True
                                        elif re.search("\s" + item.get_text().replace("_", " ") + "$", item1.get_text().replace("_", " "), re.IGNORECASE):
                                            connections["matches"].append([i.name, item.get_text(), j.name, item1.get_text(), " share part of the label\n", "rdfs:subClassOf"])
                                            already_matched = True
                                        elif re.match("^" + item1.get_text().replace("_", " ") + "\s", item.get_text().replace("_", " "), re.IGNORECASE):
                                            connections["matches"].append([i.name, item.get_text(), j.name, item1.get_text(), " share part of the label\n", "dcterms:partOf"])
                                            already_matched = True
                                        elif re.search("\s" + item1.get_text().replace("_", " ") + "$", item.get_text().replace("_", " "), re.IGNORECASE):
                                            connections["matches"].append([i.name, item.get_text(), j.name, item1.get_text(), " share part of the label\n", "rdfs:subClassOf"])
                                            already_matched = True
                    #comment = i.get_child("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}comment")
                    #if comment != None:
                    #    match_result = re.match(".*" + comment.get_text() + ".*", j.name, re.IGNORECASE)
                    #    if match_result:
                    #        util.write2File("matching.txt", "Nodes " + i.name + " and " + j.name + " are similar, because of the comment\n", "a")
            except re.error:
                #just ignore errors during regular expression operations and try to go on
                pass
        return results.append(connections)