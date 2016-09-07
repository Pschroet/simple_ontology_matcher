'''
Created on 12.08.2016

@author: Philipp Schroeter
'''

import imp
import logging
import os

# This class is a wrapper for reading ontologies
# - first the file will be tested, to see if there is a known file format
# - if one is found, then this module will be loaded dynamically, using 'imp', the module needs a function called 'parse_ontology_file' to parse the file, which takes on argument: the root element
# - then the file will be given to this module and the function 'parse_ontology_file' will be called
# - the expected return value is an object with type 'ontology', either empty or filled with the ontology read from the file
class ontology_reader(object):
    
    file = ""
    parser_module = ""
    ontology = ""
    
    def __init__(self, reader, ontology_file):
        self.file = ontology_file
        try:
            self.parser_module = imp.load_source(reader, os.path.dirname(__file__) + '/reader/' + reader + ".py")
            print "Loading " + str(self.parser_module)
            self.ontology = self.parser_module.parse_ontology_file(ontology_file)
        except ImportError as err:
            logging.error("Failed to load module " + reader + ":")
            logging.error(err)