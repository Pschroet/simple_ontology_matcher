'''
Created on 13.08.2016

@author: Philipp Schroeter
'''

import onto_element
import ontology
import os
import util

def parse_ontology_file(ontology_tree):
    #get the name of the ontology
    base_element = ontology_tree.find("{http://www.w3.org/2002/07/owl#}Ontology")
    onto = ontology.ontology(base_element.attrib["{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about"].replace("{http://www.w3.org/2002/07/owl#}", ""))
    tempProps = []
    tempElems = []
    #go through all elements
    for item in ontology_tree:
        #print item
        #get the properties of the ontology
        if item.tag == "{http://www.w3.org/2002/07/owl#}ObjectProperty":
            new_prop = onto_element.onto_elem(item.attrib["{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about"], item.tag.replace("{http://www.w3.org/2002/07/owl#}", ""), item.text)
            tempProps.append(new_prop)
        #get all class elements
        elif item.tag == "{http://www.w3.org/2002/07/owl#}Class":
            #create a new ontology element
            elem = onto_element.onto_elem(item.attrib["{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about"], item.tag.replace("{http://www.w3.org/2002/07/owl#}", ""), item.text)
            #util.write2File("test1.txt", "Created " + item.attrib["{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about"] + ": " + str(elem) + "\n", "a")
            for attr in item.attrib:
                elem.add_attribute(attr, item.attrib[attr])
            #get the children
            add_children(elem, item.getchildren())
            tempElems.append(elem)
        #if the ontology is populated with individuals, get them, too
        elif item.tag == "{http://www.w3.org/2002/07/owl#}NamedIndividual":
            #create a new ontology element
            elem = onto_element.onto_elem(item.attrib["{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about"], item.tag.replace("{http://www.w3.org/2002/07/owl#}", ""), item.text)
            #util.write2File("test1.txt", "Created " + item.attrib["{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about"] + ": " + str(elem) + "\n", "a")
            for attr in item.attrib:
                elem.add_attribute(attr, item.attrib[attr])
            #get the children
            add_children(elem, item.getchildren())
            tempElems.append(elem)
    if onto != "" and len(tempProps) > 0:
        onto.add_properties(tempProps)
    if onto != "" and len(tempElems) > 0:
        onto.add_elements(tempElems)
    if onto != "":
        #util.write2File("onto.txt", str(onto) + os.linesep, "a")
        #util.write2File("onto.txt", str(onto.get_elements()) + os.linesep, "a")
        return onto
    else:
        return ""

#goes recursively through all children of a given node
#adds the children of the given node and their children as onto_elem objects to the given node
def add_children(node, children):
    for child in children:
        new_elem = onto_element.onto_elem(child.tag,  child.tag.split("}")[-1], child.text)
        if len(child.getchildren()) > 0:
            add_children(new_elem, child)
        node.add_child(new_elem)