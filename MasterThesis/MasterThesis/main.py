'''
Created on 13.08.2016

@author: Philipp Schroeter
'''

import matching_tool_chain
import reader
#import matcher

if __name__ == '__main__':
    r = reader.ontology_reader("owl_rdfxml_parser", "/home/philipp/Dokumente/Ontologie/AnimalMotionOntology.owl")
    r1 = reader.ontology_reader("owl_rdfxml_parser", "/home/philipp/Dokumente/Ontologie/envo.owl")
    #chain = matching_tool_chain.tool_chain("./hs-config.xml")
    chain = matching_tool_chain.tool_chain("./test-config.xml")
    chain.match_ontologies([r.ontology, r1.ontology])
    #r = reader.ontology_reader("owl_rdfxml_parser", "cafe.owl")
    #r1 = reader.ontology_reader("owl_rdfxml_parser", "envo.owl")
    #chain = matching_tool_chain.tool_chain("./test-config.xml")
    #chain.match_ontologies([r.ontology, r1.ontology])