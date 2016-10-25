'''
Created on 24.10.2016

@author: Philipp Schroeter
'''

import defusedxml.ElementTree
import matching
import re

def parse_ontology_file(ontology_file):
    print "Parsing " + ontology_file
    tree = defusedxml.ElementTree.parse(ontology_file)
    root = tree.getroot()
    #check if the file could even be an OWL file in RDF XML syntax
    if root.tag == "Alignment":
        matchings = matching.matchings()
        children = root.findall("Cell").getchildren()
        for child in children:
            if re.match("entity[0-9]*", child.tag, re.IGNORECASE):
                matchings.add_element(child)
            elif re.match("measure", child.tag, re.IGNORECASE):
                matchings.add_property(child)
            elif re.match("relation", child.tag, re.IGNORECASE):
                matchings.add_property(child)