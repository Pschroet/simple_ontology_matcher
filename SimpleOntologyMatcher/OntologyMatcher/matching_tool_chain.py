'''
Created on 31.08.2016

@author: Philipp Schroeter
'''

import defusedxml.ElementTree
import matcher

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
            if item.tag == "matcher":
                self.matching_tools.append(item.text)

    def add_matchers(self, matchers = []):
        if matchers != []:
            self.matching_tools = matchers

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