'''
Created on 14.08.2016

@author: Philipp Schroeter
'''

import os

class ontology(object):
    '''
    A class to save an ontology
    '''
    name = ""
    namespaces = {}
    properties = []
    elements = []
    
    def __init__(self, name):
        self.name = name
        self.properties = []
        self.elements = []

    def get_name(self):
        return self.name
    
    def add_namespace(self, abbreviation, namespace):
        self.namespaces[abbreviation] = namespace
    
    def get_namespaces(self):
        return self.namespaces
    
    def add_element(self, elem):
        self.elements.append(elem)
    
    def add_elements(self, elems):
        for elem in elems:
            self.add_element(elem)
    
    def get_elements(self):
        return self.elements
    
    def add_property(self, prop):
        self.properties.append(prop)
    
    def add_properties(self, props):
        for prop in props:
            self.add_property(prop)
    
    def get_properties(self):
        return self.properties
    
    def tostring(self):
        output = "Ontology " + self.name + ":" + os.linesep
        if len(self.namespaces) > 0:
            output = output + "Namespaces:" + os.linesep
            for namespace in self.namespaces:
                output = output + "\t-> " + namespace + " " + self.namespaces[namespace] + os.linesep
        if len(self.properties) > 0:
            output = output + "Properties:" + os.linesep
            for prop in self.properties:
                output = output + "\t-> " + str(prop) + os.linesep
        if len(self.elements) > 0:
            output = output + "Elements:" + os.linesep
            for elem in self.elements:
                output = output + "\t-> " + elem.tostring(level=1)