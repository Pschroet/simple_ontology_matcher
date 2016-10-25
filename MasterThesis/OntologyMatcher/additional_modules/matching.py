'''
Created on 25.10.2016

@author: Philipp Schröter
'''

class matchings(object):
    '''
    A class to save a matching of two or more ontologies
    '''
    elements = []
    properties = []
    
    def __init__(self):
        pass
        
    def add_element(self, element):
        self.elements.append(element)
    
    def add_elements(self, elements):
        self.elements = self.elements + elements
        
    def add_property(self, prop):
        self.properties.append(prop)
    
    def add_properties(self, properties):
        self.properties = self.properties + properties