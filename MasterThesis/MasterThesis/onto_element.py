'''
Created on 14.08.2016

@author: Phil
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

    def get_namespace(self, namespace):
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

    #searches a child with the given name
    #returns None, if there is no child with this name
    def get_child(self, name):
        for item in self.children:
            if item.name == name:
                return item
        return None

    def get_children(self):
        return self.children
    
    def add_attribute(self, key, value):
        #util.write2File("test1.txt", "\tadding attribute " + str(key) + ":" + value + " (" + str(self) + ")\n", "a")
        self.attributes[key] = value

    def get_attribute(self, key):
        if key in self.attributes:
            return self.attributes(key)

    def get_attributes(self):
        return self.attributes

    def tostring(self):
        output = "Element: " + self.name + os.linesep
        output = output + "-> Attributes: " + self.attributes + os.linesep
        output = output + "-> Children: " + self.children
        #util.write2File("test.txt", output, "a")
        return output