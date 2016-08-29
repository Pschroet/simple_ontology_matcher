'''
Created on 12.08.2016

@author: Philipp Schroeter
'''

import defusedxml.ElementTree
import imp
import logging
import os
import util

# This class is a wrapper for reading ontologies
# - first the file will be tested, to see if there is a known file format
# - if one is found, then this module will be loaded dynamically, using 'imp', the module needs a function called 'parse_ontology_file' to parse the file, which takes on argument: the root element
# - then the file will be given to this module and the function 'parse_ontology_file' will be called
# - the expected return value is an object with type 'ontology', either empty or filled with the ontology read from the file
class ontology_reader(object):
    
    file = ""
    tree = ""
    parser_module = ""
    ontology = ""
    
    def __init__(self, ontology_file):
        self.file = ontology_file
        self.tree = defusedxml.ElementTree.parse(self.file)
        root = self.tree.getroot()
        #parse the file and look, if the format can be detected
        if root.tag == "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF":
            children = root.findall("{http://www.w3.org/2002/07/owl#}Ontology")
            #look if there is exactly one 'Ontology' element from namespace 'owl'
            if len(children) == 1 and children[0].tag.replace("{", "").replace("}", "").replace("#", ""):
                used_parser = "owl_rdfxml_parser"
            #load the parser
            if used_parser != "":
                try:
                    self.parser_module = imp.load_source(used_parser, './' + used_parser + ".py")
                    print "Loading " + str(self.parser_module)
                    self.ontology = self.parser_module.parse_ontology_file(root)
                except ImportError as err:
                    logging.error("Failed to load module " + used_parser + ":")
                    logging.error(err)