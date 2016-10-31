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
            if comparison.is_same(matching.elements):
                same.append(matching.elements)
            else:
                different.append(matching.elements)
    #print "same: " + str(same)
    #print "different: " + str(different)
    return [same, different]