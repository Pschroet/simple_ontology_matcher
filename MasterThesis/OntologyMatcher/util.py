'''
Created on 18.08.2016

A collection of different support functions

@author: Philipp Schroeter
'''

import cgi
import logging
import imp
import json
import os
import re
import requests
import sys
from django.conf import settings
from operator import itemgetter

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

def get_files_in_directory(directory, recursive):
    output = []
    content = os.listdir(directory)
    for item in content:
        tmp = directory + "/" + item
        if os.path.isfile(tmp):
            output.append(item)
        elif os.path.isdir(tmp) and recursive:
            output = output + get_files_in_directory(tmp, True)
    return output

#filters all elements from a list, where the given filter is found as part of a regex
#returns a list with the elements removed
def filter_files_from_list(file_list, expr):
    output = []
    for elem in file_list:
        if not re.match(".*" + expr + ".*", elem):
            output.append(elem)
    return output

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

def get_ontologies():
    return settings.ONTOLOGIES

def get_terminologies():
    return settings.TERMINOLOGIES

def get_matchers():
    return settings.MATCHERS

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
            try:
                string1 = string1.encode('utf8')
            except UnicodeEncodeError:
                pass
            try:
                string2 = string2.encode('utf8')
            except UnicodeEncodeError:
                pass
            return self.Levenshtein.distance(string1, string2)
        else:
            return levenshtein(string1, string2)

#moves all elements from dict1 to dict
# items are excluded, if there is already an element named like one in dict
#returns the result as a new dictionary
def combine_dicts(dict, dict1):
    output = {}
    for item in dict:
        output[item] = dict[item]
    for item in dict1:
        if item not in dict:
            output[item] = dict1[item]
    return output

class dictionary_wrapper():
    PyDictionary_found = False
    PyDictionary = ""
    
    def __init__(self):
        #test if  PyDictionary module is installed and if it is, import it
        try:
            imp.find_module('PyDictionary')
            self.PyDictionary = __import__('PyDictionary').PyDictionary()
            self.PyDictionary_found = True
        except ImportError:
            logging.error("PyDictionary module not found, using own implementation")

    def synonym(self, string):
        if self.PyDictionary_found:
            return self.PyDictionary.synonym(string)
        else:
            return ""

    def antonym(self, string):
        if self.PyDictionary_found:
            return self.PyDictionary.antonym(string)
        else:
            return ""