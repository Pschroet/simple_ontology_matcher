'''
Created on 29.08.2016

@author: Philipp Schroeter
'''

import logging
import imp

class ontology_writer(object):
    
    output_module = ""
    ontology = ""
    
    def __init__(self, writer, destination_file = "", ontology = None):
        if destination_file != "" and ontology != None:
            try:
                self.output_module = imp.load_source(writer, './' + writer + ".py")
                print "Loading " + str(self.parser_module)
                self.ontology = self.parser_module.write_ontology_file(destination_file, ontology)
            except ImportError as err:
                logging.error("Failed to load module " + writer + ":")
                logging.error(err)