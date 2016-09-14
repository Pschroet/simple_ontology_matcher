'''
Created on 14.09.2016

@author: Philipp Schroeter
'''

import matching_tool_chain
import matcher

def match_two_ontologies(onto, onto1):
    results = []
    chain = matching_tool_chain.tool_chain()
    chain.add_config_from_file("./all_matchers-config.xml")
    for matching_tool in chain.matching_tools:
                tmp_tool = matcher.ontology_matcher(matching_tool)
                results.append(tmp_tool.match_two_ontologies([onto, onto1]))