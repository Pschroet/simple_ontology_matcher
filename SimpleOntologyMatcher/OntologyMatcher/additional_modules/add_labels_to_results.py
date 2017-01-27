'''
Created on 27.01.2017

@author: Philipp Schroeter
'''

import reader
import xmlrdf_result_reader

#searches for labels in the given ontologies to add them to the matchings
# returns the new matchings (instance of class matching) with added labels, for the elements where they could be found
def add_labels(ontology_reader_used1, ontology_file1, ontology_reader_used2, ontology_file2, matching_result_file):
    ontology1 = reader.ontology_reader(ontology_reader_used1, ontology_file1).ontology
    ontology2 = reader.ontology_reader(ontology_reader_used2, ontology_file2).ontology
    matchings = xmlrdf_result_reader.parse_matchings_file(matching_result_file)
    for matching in matchings:
        matching_elem1, matching_elem2 = matching.get_elements()
        #try to find the first element in one of the two ontologies
        elem1 = ontology1.get_element_named(matching_elem1)
        if elem1 is None:
            elem1 = ontology2.get_element_named(matching_elem1)
        elem2 = ontology1.get_element_named(matching_elem2)
        if elem2 is None:
            elem2 = ontology2.get_element_named(matching_elem2)
        #try to get the labels and add them to the matching
        temp = []
        if elem1 is not None:
            label1 = elem1.get_child("{http://www.w3.org/2000/01/rdf-schema#}label")
            if label1 is not None:
                temp.append(["{http://www.w3.org/2000/01/rdf-schema#}label", label1.get_text()])
            else:
                temp.append([])
        if elem2 is not None:
            label2 = elem2.get_child("{http://www.w3.org/2000/01/rdf-schema#}label")
            if label2 is not None:
                temp.append(["{http://www.w3.org/2000/01/rdf-schema#}label", label2.get_text()])
            else:
                temp.append([])
        matching.add_properties(temp)
    return matchings