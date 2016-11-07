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
    
    #add a property as a key value pair
    def add_property(self, key, value):
        self.properties.append([key, value])
    
    #add an amount of properties from a dictionary
    def add_properties(self, properties):
        self.properties = self.properties + properties
    
    #returns the value of a key value pair in the properties of this matching object
    # if no property with the given key is found, None is returned
    # if there is more than one property with the given key the first is returned
    def get_property_named(self, key):
        for prop in self.properties:
            if prop[0] == key:
                return prop[1]
        return None
    
    #returns all list of all values of a key value pair in the properties of this matching object
    # if no property with the given key is found, None is returned
    # even if only one item is returned, still a list will be returned
    def get_properties_named(self, key):
        output = []
        for prop in self.properties:
            if prop[0] == key:
                output.append(prop[1])
        if len(output) > 0:
            return output
        else:
            return None
    
    #empties a copy of the elements of this object
    # if there are no elements left, then True is returned
    # if there is an element in the given elements, that is not in the one of this object, False is returned
    # if there are elements left, False is returned
    def is_same(self, comp_elements):
        #print "Comparing " + str(self.elements) + " with " + str(comp_elements)
        tmp = set(self.elements)
        tmp1 = set(comp_elements)
        diff =  tmp - tmp1
        if len(tmp) == len(tmp1) and len(diff) == 0:
            return True
        else:
            return False
    
    def tostring(self):
        return "Elements: " + str(self.elements) + ", Properties: " + str(self.properties)