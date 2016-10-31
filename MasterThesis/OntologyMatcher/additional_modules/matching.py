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
    properties = []
    
    def __init__(self):
        pass
    
    #add a single element
    def add_element(self, element):
        self.elements.append(element)
    
    #add multiple elements as a list
    def add_elements(self, elements):
        self.elements = self.elements + elements
    
    def has_element(self, element):
        if element in self.elements:
            return True
        else:
            return False
    
    #empties a copy of the elements of this object
    # if there are no elements left, then True is returned
    # if there is an element in the given elements, that is not in the one of this object, False is returned
    # if there are elements left, False is returned
    def is_same(self, elements):
        #print "Comparing " + str(elements) + " with " + str(self.elements)
        tmp = list(self.elements)
        for elem in elements:
            try:
                tmp.remove(elem)
            except ValueError:
                return False
        try:
            tmp.pop()
            return False
        except IndexError:
            return True
    
    #add a property as a key value pair
    def add_property(self, key, value):
        self.properties.append([key, value])
    
    #add an amount of properties from a dictionary
    def add_properties(self, properties):
        self.properties = self.properties + properties
    
    def tostring(self):
        return "Elements: " + str(self.elements) + ", Properties: " + str(self.properties)