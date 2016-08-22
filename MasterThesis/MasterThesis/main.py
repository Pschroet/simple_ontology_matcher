'''
Created on 13.08.2016

@author: Philipp Schroeter
'''

import reader
import matcher

if __name__ == '__main__':
    #r = reader.ontology_reader("cafe-test.owl")
    r = reader.ontology_reader("cafe.owl")
    #r1 = reader.ontology_reader("envo-test.owl")
    r1 = reader.ontology_reader("envo.owl")
    matcher.ontology_matcher("simple_label_matcher", [r.ontology, r1.ontology])