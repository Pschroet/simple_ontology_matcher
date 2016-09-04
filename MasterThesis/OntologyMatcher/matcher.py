'''
Created on 19.08.2016

@author: Phil
'''

import imp
import logging

class ontology_matcher(object):
    '''
    classdocs
    '''

    matcher_module = ""
    onto = ""
    ontologies = []

    def __init__(self, matcher, ontologies):
        '''
        Constructor
        '''
        if matcher != "" and ontologies != None and ontologies != "":
            try:
                self.matcher_module = imp.load_source(matcher, './matcher/' + matcher + ".py")
                print "Loading " + str(self.matcher_module)
                self.ontologies = ontologies
            except ImportError as err:
                logging.error("Failed to load module " + matcher + ":")
                logging.error(err)

    def match_two_ontologies(self):
        self.onto = self.matcher_module.match_two_ontologies(self.ontologies[0], self.ontologies[1])