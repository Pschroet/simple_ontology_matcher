'''
Created on 25.10.2016

@author: Philipp Schroeter
'''

class matching(object):
    '''
    A class to save a matching of two or more elements, contains
    - the elements themself of the matching (just a list of elements, usually strings)
    - the properties of the matching (expected is a dictionary)
    '''
    elements = []
    properties = {}
    
    def __init__(self):
        pass
    
    #add a single element
    def add_element(self, element):
        self.elements.append(element)
    
    #add multiple elements as a list
    def add_elements(self, elements):
        self.elements = self.elements + elements
    
    #add a property as a key value pair
    def add_property(self, key, value):
        self.properties[key] = value
    
    #add an amount of properties from a dictionary
    def add_properties(self, properties):
        for prop in properties:
            self.properties[prop] = properties[prop]
    
    def tostring(self):
        output = "Elements: " + str(self.elements)
        for prop in self.properties:
            output = output + ", Property: " + prop + ": " + self.properties[prop]
        return output