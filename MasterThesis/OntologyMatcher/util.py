'''
Created on 18.08.2016

A collection of different support functions

@author: Philipp Schroeter
'''

import logging
import imp
import os

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

#checks if the given file exists
#  if it does not exist, but the directory can be written to the file will be created
def checkFile(fileToCheck, create):
    directory = os.path.dirname(os.path.realpath(fileToCheck))
    #print "[util.checkFile] Directory " + directory
    if os.path.exists(directory):
        if os.path.isfile(fileToCheck):
            #print "[util.checkFile] Object " + fileToCheck + " found"
            return True
        else:
            if create:
                #print "[util.checkFile] Object " + fileToCheck + " does not exist, it will be created"
                openedFile = open(fileToCheck, "w")
                openedFile.close()
                return True
            else:
                #print "[util.checkFile] Object " + fileToCheck + " does not exist"
                return False
    else:
        #print "[util.checkFile] Directory of file " + fileToCheck + " does not exist or cannot be accessed"
        return False
    #to ensure something is returned
    return False

def write2File(filename, content, mode):
    f = open(filename, mode)
    f.write(content.encode('utf-8'))
    f.close()

#returns the content of a file as a list or "" if there is no content
# note: removes line separators
def readFileContentAsList(fileToRead):
    if checkFile(fileToRead, False):
        openedFile = open(fileToRead, "r")
        content = openedFile.readlines()
        #remove newlines
        for i in range(0, len(content)):
            content[i] = content[i].rstrip(os.linesep)
        openedFile.close()
        return content
    return ""

#returns the content of a file as a String or "" if there is no content
def readFileContentAsString(fileToRead):
    if checkFile(fileToRead, False):
        openedFile = open(fileToRead, "r")
        contentLines = openedFile.readlines()
        content = ""
        #concat lines
        for i in range(0, len(contentLines)):
            content = content + contentLines[i]
        openedFile.close()
        return content
    return ""

#calculates the Levenshtein distance
# source: https://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Levenshtein_distance#Python
def levenshtein(s1, s2):
    if len(s1) < len(s2):
        return levenshtein(s2, s1)

    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1       # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    
    return previous_row[-1]

class distance_calculator():
    
    levenshtein_found = False
    Levenshtein = ""
    
    def __init__(self):
        #test if  levenshtein module is installed and if it is, import it
        try:
            imp.find_module('Levenshtein')
            self.Levenshtein = __import__('Levenshtein')
            self.levenshtein_found = True
        except ImportError:
            logging.error("Levenshtein module not found, using own implementation")

    def calculate_distance(self, string1, string2):
        if self.levenshtein_found:
            return self.Levenshtein.distance(string1, string2)
        else:
            return levenshtein(string1, string2)