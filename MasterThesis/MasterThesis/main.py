'''
Created on 13.08.2016

@author: Philipp Schroeter
'''

import reader
import matcher

if __name__ == '__main__':
    r = reader.ontology_reader("owl_rdfxml_parser", "/home/philipp/Dokumente/Ontologie/AnimalMotionOntology.owl")
    r1 = reader.ontology_reader("owl_rdfxml_parser", "/home/philipp/Dokumente/Ontologie/envo.owl")
    matcher.ontology_matcher("hs_matcher", [r.ontology, r1.ontology])
    #r = reader.ontology_reader("owl_rdfxml_parser", "cafe.owl")
    #r1 = reader.ontology_reader("owl_rdfxml_parser", "envo.owl")
    #matcher.ontology_matcher("simple_label_matcher", [r.ontology, r1.ontology])