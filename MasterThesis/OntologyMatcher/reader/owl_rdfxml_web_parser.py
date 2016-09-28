'''
Created on 28.09.2016

@author: Philipp Schroeter
'''

import defusedxml
import ontology
import onto_element
import re
import requests

def parse_ontology_file(ontology_url):
    ontology_content = requests.get(ontology_url)
    print ontology_content.headers
    print len(ontology_content.content)
    #print ontology_content
    root = defusedxml.ElementTree.fromstring(ontology_content.text.encode('utf8'))
    #check if the file could even be an OWL file in RDF XML syntax
    if root.tag == "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF":
        onto_info = root.findall("{http://www.w3.org/2002/07/owl#}Ontology")
        #look if there is exactly one 'Ontology' element from namespace 'owl'
        if onto_info[0].tag.replace("{http://www.w3.org/2002/07/owl#}", "") == "Ontology":
            #get the name of the ontology
            onto = ontology.ontology(onto_info[0].attrib["{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about"])
            tempProps = []
            tempElems = []
            #go through all elements
            for item in root.getchildren():
                #get the properties of the ontology
                if re.match("{http://www.w3.org/2002/07/owl#}.*Property", item.tag):
                    new_prop = onto_element.onto_elem(item.attrib["{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about"], item.tag.replace("{http://www.w3.org/2002/07/owl#}", ""), item.text)
                    add_children(new_prop, item.getchildren())
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
            #get the namespaces from the RDF element (the root) and put them into the ontology
            for attr in root.attrib:
                onto.add_namespace(attr, root.attrib[attr])
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
        for attr in child.attrib:
            new_elem.add_attribute(attr, child.attrib[attr])
        if len(child.getchildren()) > 0:
            add_children(new_elem, child)
        node.add_child(new_elem)