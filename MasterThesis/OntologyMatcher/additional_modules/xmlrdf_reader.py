'''
Created on 24.10.2016

@author: Philipp Schroeter
'''

import defusedxml.ElementTree
import matching
import re

def parse_matchings_file(matchings_file):
    print "Parsing matching file " + matchings_file
    tree = defusedxml.ElementTree.parse(matchings_file)
    root = tree.getroot().find("{http://knowledgeweb.semanticweb.org/heterogeneity/alignment}Alignment")
    #check if the file could even be an OWL file in RDF XML syntax
    if root.tag == "{http://knowledgeweb.semanticweb.org/heterogeneity/alignment}Alignment":
        matchings = []
        maps = root.findall("{http://knowledgeweb.semanticweb.org/heterogeneity/alignment}map")
        #print maps
        for map_ in maps:
            children = map_.find("{http://knowledgeweb.semanticweb.org/heterogeneity/alignment}Cell").getchildren()
            #print "Element: " + str(map_)
            #print "-> " + str(children)
            match = matching.matching()
            tmp_elements = []
            tmp_properties = []
            for child in children:
                #print "-> " + str(child)
                if re.match("[{]http[:][/][/]knowledgeweb[.]semanticweb[.]org[/]heterogeneity[/]alignment[}]entity[0-9]*", child.tag, re.IGNORECASE):
                    tmp_elements.append(child.attrib["{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource"])
                elif re.match("[{]http[:][/][/]knowledgeweb[.]semanticweb[.]org[/]heterogeneity[/]alignment[}]measure", child.tag, re.IGNORECASE):
                    tmp_properties.append([child.tag, child.text])
                elif re.match("[{]http[:][/][/]knowledgeweb[.]semanticweb[.]org[/]heterogeneity[/]alignment[}]relation", child.tag, re.IGNORECASE):
                    tmp_properties.append([child.tag, child.text])
                #get the label if the entity has one
                label = child.find("{http://www.w3.org/2000/01/rdf-schema#}label")
                #print label.text
                if label is not None and label is not "":
                    tmp_properties.append(["{http://www.w3.org/2000/01/rdf-schema#}label", label.text])
            match.add_elements(tmp_elements)
            match.add_properties(tmp_properties)
            #print match.tostring()
            matchings.append(match)
        #print matchings
        return matchings