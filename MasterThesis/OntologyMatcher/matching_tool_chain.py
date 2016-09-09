'''
Created on 31.08.2016

@author: philipp
'''

import defusedxml.ElementTree
import matcher

class tool_chain(object):
    '''
    classdocs
    '''

    config = ""
    matching_tools = []
    ontologies = []

    def __init__(self, config):
        '''
        Constructor
        '''
        self.config = config
        tree = defusedxml.ElementTree.parse(self.config)
        root = tree.getroot()
        for item in root.getchildren():
            if item.tag == "matcher":
                self.matching_tools.append(item.text)

    #read an ontology
    def match_ontologies(self, ontologies = []):
        results = {}
        if len(ontologies) > 2:
            print "[Error] At least two ontologies needed to compare"
        elif len(ontologies) == 2:
            for matching_tool in self.matching_tools:
                tmp_tool = matcher.ontology_matcher(matching_tool, ontologies)
                result = tmp_tool.match_two_ontologies()
                #collect the results
                for key in result:
                    if results.has_key(key):
                        results[key] = results[key] + result[key]
                    else:
                        results[key] = result[key]
        return results