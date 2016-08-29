'''
Created on 29.08.2016

@author: Philipp Schroeter
'''

import onto_element
import ontology
import os
import util

def write_ontology_file(destination_file, ontology):
    output = "<?xml version=\"1.0\"?>" + os.linesep + "<rdf:RDF "
    #add the namespaces if there are any, which they should
    namespaces = ontology.get_namespaces()
    if len(namespaces) > 0:
        for namespace in namespaces:
            output = output + namespace + "=\"" + namespaces[namespace] + "\"" + os.linesep
    #close the opening RDF tag and add the Ontology tag
    output = output + ">" + os.linesep + "\t<owl:Ontology rdf:about=\"" + ontology.get_name() + "\"/>" + os.linesep
    props = ontology.get_properties()
    if len(props) > 0:
        output = output + "<!-- Properties -->" + os.linesep
        for prop in props:
            pass