'''
Created on 14.08.2016

@author: Philipp Schroeter
'''

class ontology(object):
    '''
    A class to save an ontology
    '''
    name = ""
    properties = []
    elements = []
    
    def __init__(self, name):
        self.name = name
        self.properties = []
        self.elements = []

    def get_name(self):
        return self.name
    
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