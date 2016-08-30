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
            #define a text that will be the header of a matching, if a match is found this text will change, if it hasn't changed, do not write it into the file
            start_text = "Node " + i.name + "\n"
            #this is the text that the matchings will be added to and written, if it does change from this point
            matching_text = start_text
            try:
                #look for case insensitive, but exact matches between labels
                for j in onto1_elements:
                    labels = i.get_children_named("{http://www.w3.org/2000/01/rdf-schema#}label")
                    for label in labels:
                        src_label = label.get_text()
                        labelChildren = j.get_children_named("{http://www.w3.org/2000/01/rdf-schema#}label")
                        if(len(labelChildren) > 0) and label.get_attribute("{http://www.w3.org/XML/1998/namespace}lang") == "en" and string.upper(src_label) == string.upper(labelChildren[0].get_text()):
                            matching_text = matching_text + "  -> " + j.name + " has the same label: '" + src_label + "'\n"
                #check the label using regular expressions
                for j in onto1_elements:
                    labels = i.get_children_named("{http://www.w3.org/2000/01/rdf-schema#}label")
                    for label in labels:
                        src_label = label.get_text()
                        dest_label = j.get_children_named("{http://www.w3.org/2000/01/rdf-schema#}label")[0].get_text()
                        match_result = re.match(src_label, dest_label, re.IGNORECASE)
                        if match_result:
                            matching_text = matching_text + "  -> " + j.name + " has part of the label '" + src_label + "' in it's own one: '" + dest_label + "'\n"
                    #comment = i.get_child("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}comment")
                    #if comment != None:
                    #    match_result = re.match(".*" + j.name.replace("http://purl.obolibrary.org/obo/", "") + ".*", comment.get_text(), re.IGNORECASE)
                    #    if match_result:
                    #        util.write2File("matching.txt", "Nodes " + i.name + " and " + j.name + " are similar, because of the comment\n", "a")
                if not start_text == matching_text:
                    util.write2File("matching.txt", matching_text, "a")
            except re.error:
                #just ignore errors during regular expression operations and try to go on
                pass