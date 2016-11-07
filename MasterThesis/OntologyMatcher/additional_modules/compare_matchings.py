'''
Created on 26.10.2016

@author: Philipp Schroeter
'''

#compares two matchings and returns a list for all matchings that are in both of them
# returns two lists, the first with all matchings that are equal, the second for all which are different
def compare(matching1, matching2):
    same = []
    different = []
    for matching in matching1:
        for comparison in matching2:
            #print str(matching.elements) + " == " + str(comparison.elements)
            tmp = ""
            if matching.is_same(comparison.elements):
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
                same.append(tmp)
            else:
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
                different.append(tmp)
    #print "same: " + str(same)
    #print "different: " + str(different)
    return [same, different]