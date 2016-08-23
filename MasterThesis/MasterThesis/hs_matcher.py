'''
Created on 23.08.2016

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
                #util.write2File("regex.txt", i.name.replace("http://www.semanticweb.org/christianstein/ontologies/2014/4/untitled-ontology-59#", "") + ":" + "\n", "a")
                #if i.get_child("{http://www.w3.org/2000/01/rdf-schema#}label") != None:
                #    util.write2File("regex.txt", "-> " + i.get_child("{http://www.w3.org/2000/01/rdf-schema#}label").get_text() + "\n", "a")
                #if i.get_child("{http://www.w3.org/2000/01/rdf-schema#}comment") != None:
                #    util.write2File("regex.txt", "-> " + i.get_child("{http://www.w3.org/2000/01/rdf-schema#}comment").get_text() + "\n", "a")
                for j in onto1_elements:
                    match_result = re.match(".*" + i.name.replace("http://www.semanticweb.org/christianstein/ontologies/2014/4/untitled-ontology-59#", "") + ".*", j.name, re.IGNORECASE)
                    if match_result:
                        util.write2File("matching.txt", "Nodes " + i.name + " and " + j.name + " are similar, because of the name\n", "a")
                    labels = i.get_children_named("{http://www.w3.org/2000/01/rdf-schema#}label")
                    for label in labels:
                        match_result = re.match(".*" + label.get_text() + ".*", j.get_children_named("{http://www.w3.org/2000/01/rdf-schema#}label")[0].get_text(), re.IGNORECASE)
                        if match_result:
                            util.write2File("matching.txt", "Nodes " + i.name + " (" + label.get_text() + ") and " + j.name + " (" + j.get_children_named("{http://www.w3.org/2000/01/rdf-schema#}label")[0].get_text() + ")" + " are similar, because of the label" + "\n", "a")
                    #comment = i.get_child("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}comment")
                    #if comment != None:
                    #    match_result = re.match(".*" + j.name.replace("http://purl.obolibrary.org/obo/", "") + ".*", comment.get_text(), re.IGNORECASE)
                    #    if match_result:
                    #        util.write2File("matching.txt", "Nodes " + i.name + " and " + j.name + " are similar, because of the comment\n", "a")
            except re.error:
                pass
        #print "Going through ontology " + onto1.name
        #for k in onto1_elements:
        #    try:
        #        util.write2File("regex.txt", k.name + ":" + "\n", "a")
        #        if k.get_child("{http://www.w3.org/2000/01/rdf-schema#}label") != None:
        #            util.write2File("regex.txt", "-> " + k.get_child("{http://www.w3.org/2000/01/rdf-schema#}label").get_text() + "\n", "a")
        #        if k.get_child("{http://www.w3.org/2000/01/rdf-schema#}comment") != None:
        #            util.write2File("regex.txt", "-> " + k.get_child("{http://www.w3.org/2000/01/rdf-schema#}comment").get_text() + "\n", "a")
        #        for l in onto_elements:
        #            match_result1 = re.match(".*" + k.name + ".*", l.name, re.IGNORECASE)
        #            if match_result1:
        #                util.write2File("matching.txt", "Nodes " + k.name + " and " + l.name + " are similar, because of the name\n", "a")
        #            label1 = k.get_child("{http://www.w3.org/2000/01/rdf-schema#}label")
        #            if label1 != None:
        #                match_result1 = re.match(".*" + label1.get_text() + ".*", l.name, re.IGNORECASE)
        #                if match_result1:
        #                    util.write2File("matching.txt", "Nodes " + k.name + " and " + l.name + " are similar, because of the label: " + label1.get_text() + "\n", "a")
        #            comment1 = k.get_child("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}comment")
        #            if comment1 != None:
        #                match_result1 = re.match(".*" + comment1.get_text() + ".*", l.name, re.IGNORECASE)
        #                if match_result1:
        #                    util.write2File("matching.txt", "Nodes " + k.name + " and " + l.name + " are similar, because of the comment\n", "a")
        #    except re.error:
        #        pass