'''
Created on 18.08.2016

A collection of different functions

@author: Philipp Schroeter
'''

#returns the separator of the ontology element
# finds separators of namespaces that separate with '#' or '/'
# if none of these two were found an empty string is returned
def determine_separator(item):
    if item.find("#") > -1 and item.split("#")[-1] != "":
        return "#"
    elif item.find("/") > -1 and item.split("/")[-1] != "":
        return "/"
    else:
        return ""

def write2File(filename, content, mode):
    f = open(filename, mode)
    f.write(content.encode('utf-8'))
    f.close()