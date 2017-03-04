'''
Created on 31.08.2016

@author: Philipp Schroeter
'''

import defusedxml.ElementTree
import matcher
import os

class tool_chain(object):
    '''
    classdocs
    '''

    config = ""
    matching_tools = []

    def __init__(self):
        '''
        Constructor
        '''
        pass

    def add_config_from_file(self, config):
        self.config = config
        tree = defusedxml.ElementTree.parse(self.config)
        root = tree.getroot()
        for item in root.getchildren():
            if item.tag == "matcher" and os.path.isfile(os.path.dirname(__file__) + '/matcher/' + item.text + ".py"):
                self.matching_tools.append(item.text)
            else:
                print "[Error] Matcher '" + os.path.dirname(__file__) + '/reader/' + item.text + ".py' not found"

    def add_matchers(self, matchers = []):
        if matchers != []:
            for matcher in matchers:
                if os.path.isfile(os.path.dirname(__file__) + '/matcher/' + matcher + ".py"):
                    self.matching_tools.append(matcher)
                else:
                    print "[Error] Matcher '" + os.path.dirname(__file__) + '/reader/' +  + matcher + ".py' not found"

    #read an ontology
    def match_ontologies(self, ontologies = []):
        results = []
        if len(ontologies) > 2:
            print "[Error] At least two ontologies needed to compare"
        elif len(ontologies) == 2:
            for matching_tool in self.matching_tools:
                tmp_tool = matcher.ontology_matcher(matching_tool)
                tmp_tool.match_two_ontologies(results, ontologies[0], ontologies[1])
        return results