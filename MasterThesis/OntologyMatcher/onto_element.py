'''
Created on 14.08.2016

@author: Philipp Schroeter
'''

import os
import util

class onto_elem(object):
    '''
    A class for ontology elements
    '''

    name = ""
    type = ""
    namespace = ""
    text = ""
    attributes = {}
    children = []

    def __init__(self, name, elem_type, text):
        #util.write2File("test1.txt", "New elem: " + name + " (" + str(self) + ")\n", "a")
        self.name = name
        self.type = elem_type
        self.text = text
        self.attributes = {}
        self.children = []

    def get_name(self):
        return self.name
    
    def set_namespace(self, namespace):
        self.namespace = namespace
    
    def get_namespace(self):
        return self.namespace

    def get_type(self):
        return self.type

    def get_text(self):
        return self.text
    
    def add_child(self, child):
        #util.write2File("test1.txt", "\tadding child: " + str(child.name) + " to " + self.name + " (" + str(self) + ")\n", "a")
        self.children.append(child)
    
    def add_children(self, children):
        for child in children:
            self.add_child(child)

    #searches the children of this ontology element and returns the first one with the given name
    #returns None, if there is no child with this name
    #if all children should be returned, use get_children_named instead
    def get_child(self, name):
        for item in self.children:
            if item.name == name:
                return item
        return None

    def get_children(self):
        return self.children

    #returns a list of elements, with the given name
    #returns an empty list, if no element with the given name can be found
    def get_children_named(self, name):
        output = []
        for item in self.children:
            if item.name == name:
                output.append(item)
        return output
    
    def add_attribute(self, key, value):
        #util.write2File("test1.txt", "\tadding attribute " + str(key) + ":" + value + " (" + str(self) + ")\n", "a")
        self.attributes[key] = value

    #returns the attribute of this element with the given key
    # returns None with it is not found
    def get_attribute(self, key):
        if key in self.attributes:
            return self.attributes[key]
        else:
            return None

    def get_attributes(self):
        return self.attributes

    def tostring(self, level=0):
        output = ("\t" * level) + "Element: " + self.name + os.linesep
        output = output + ("\t" * level) + "-> Attributes: " + str(self.attributes) + os.linesep
        output = output + ("\t" * level) + "-> Children:\n"
        for child in self.children:
            output = output + child.tostring(level+1) + "\n"
        return output