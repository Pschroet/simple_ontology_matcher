'''
Created on 26.10.2016

@author: Philipp Schroeter
'''

import re

#compares two matchings and returns a list for all matchings that are in both of them
# returns two lists, the first with all matchings that are equal, the second for all which are different
def compare(matching1, matching2):
    same = []
    different = [[], []]
    for matching in matching1:
        matching_found = False
        for comparison in matching2:
            #print str(matching.elements) + " == " + str(comparison.elements)
            tmp = ""
            if (matching.elements[0] == comparison.elements[0] and matching.elements[1] == comparison.elements[1]) or (matching.elements[0] == comparison.elements[1] and matching.elements[1] == comparison.elements[0]):
                tmp = list(matching.elements)
                labels = matching.get_properties_named("{http://www.w3.org/2000/01/rdf-schema#}label")
                if labels is not None:
                    tmp = tmp + labels
                else:
                    labels = comparison.get_properties_named("{http://www.w3.org/2000/01/rdf-schema#}label")
                    if labels is not None:
                        tmp = tmp + labels
                #print labels
                #print tmp
                #if the matching is not already included
                if not tmp in same:
                    same.append(tmp)
                matching_found = True
        #if not matching_found and matching.elements[0] != matching.elements[1]:
        if not matching_found:
            tmp = list(matching.elements)
            labels = matching.get_properties_named("{http://www.w3.org/2000/01/rdf-schema#}label")
            if labels is not None:
                tmp = tmp + labels
            else:
                labels = comparison.get_properties_named("{http://www.w3.org/2000/01/rdf-schema#}label")
                if labels is not None:
                    tmp = tmp + labels
            #print labels
            #print tmp
            #if the matching is not already included
            if not tmp in different[0] and not tmp in different[1]:
                different[0].append(tmp)
    #check the second ontology/terminology for items not being the same
    for matching in matching2:
        matching_found = False
        for item in same:
            if (matching.elements[0] == item[0] and matching.elements[1] == item[1]) or (matching.elements[0] == item[1] and matching.elements[1] == item[0]):
                matching_found = True
        #if not matching_found and matching.elements[0] != matching.elements[1]:
        if not matching_found:
            tmp = list(matching.elements)
            labels = matching.get_properties_named("{http://www.w3.org/2000/01/rdf-schema#}label")
            if labels is not None:
                tmp = tmp + labels
            else:
                labels = comparison.get_properties_named("{http://www.w3.org/2000/01/rdf-schema#}label")
                if labels is not None:
                    tmp = tmp + labels
            #print labels
            #print tmp
            #if the matching is not already included
            if not tmp in different[0] and not tmp in different[1]:
                different[1].append(tmp)
    print "same" + "(" + str(len(same)) + ")"# + ": " + str(same)
    print "different" + "(" + str(len(different[0]) + len(different[1])) + ")"# + ": " + str(different)
    return [same, different]