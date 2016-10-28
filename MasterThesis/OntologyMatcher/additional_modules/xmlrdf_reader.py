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
            match = matching.matching()
            children = map_.find("{http://knowledgeweb.semanticweb.org/heterogeneity/alignment}Cell").getchildren()
            #print children
            for child in children:
                #print child
                if re.match("[{]http[:][/][/]knowledgeweb[.]semanticweb[.]org[/]heterogeneity[/]alignment[}]entity[0-9]*", child.tag, re.IGNORECASE):
                    match.add_element(child.attrib["{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource"])
                elif re.match("[{]http[:][/][/]knowledgeweb[.]semanticweb[.]org[/]heterogeneity[/]alignment[}]measure", child.tag, re.IGNORECASE):
                    match.add_property(child.tag, child.text)
                elif re.match("[{]http[:][/][/]knowledgeweb[.]semanticweb[.]org[/]heterogeneity[/]alignment[}]relation", child.tag, re.IGNORECASE):
                    match.add_property(child.tag, child.text)
            matchings.append(match)
        return matchings