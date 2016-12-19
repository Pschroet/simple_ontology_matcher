'''
Created on 19.12.2016

@author: Philipp Schroeter
'''

import os
import util
import xmlrdf_result_reader

#creates a CVS file with the given name and saves the information from the given matching file into the destination file
def convert(source, destination):
    matchings = xmlrdf_result_reader.parse_matchings_file(source)
    #create the file and write the header
    util.write2File(destination, "elem1,label1,elem2,label2" + os.linesep, "w")
    for matching in matchings:
        elem1 = matching.elements[0]
        elem2 = matching.elements[1]
        labels = matching.get_properties_named("{http://www.w3.org/2000/01/rdf-schema#}label")
        label1 = ""
        label2 = ""
        if labels is not None:
            if len(labels) > 0:
                label1 = labels[0]
                if len(labels) > 1:
                    label2 = labels[1]
        util.write2File(destination, elem1 + "," + label1 + "," + elem2 + "," + label2 + os.linesep, "a")