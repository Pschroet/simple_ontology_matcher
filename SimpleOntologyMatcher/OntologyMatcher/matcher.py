'''
Created on 19.08.2016

@author: Philipp Schroeter
'''

import imp
import logging
import os

class ontology_matcher(object):
    '''
    classdocs
    '''

    matcher_module = ""
    onto = ""

    def __init__(self, matcher):
        '''
        Constructor
        '''
        if matcher != "" and matcher != None:
            try:
                self.matcher_module = imp.load_source(matcher, os.path.dirname(__file__) + '/matcher/' + matcher + ".py")
                print "Loading " + str(self.matcher_module)
            except ImportError as err:
                logging.error("Failed to load module " + matcher + ":")
                logging.error(err)
            except IOError as err:
                logging.error("Could not find module " + matcher + ":")
                logging.error(err)

    def match_two_ontologies(self, results, ontology1, ontology2):
        return self.matcher_module.match_two_ontologies(results, ontology1, ontology2)