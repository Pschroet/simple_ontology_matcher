'''
Created on 13.08.2016

@author: Philipp Schroeter
'''

import matching_tool_chain
import reader
import util
import os
#import PyDictionary
from django.template import Context, Template

if __name__ == '__main__':
    #testing readers and matchers in general
    #r = reader.ontology_reader("owl_rdfxml_parser", "ontologies/AnimalMotionOntology.owl")
    #print r.ontology.tostring()
    #r1 = reader.ontology_reader("owl_rdfxml_parser", "ontologies/envo.owl")
    #chain = matching_tool_chain.tool_chain("./hs-config.xml")
    #chain = matching_tool_chain.tool_chain("./test-config.xml")
    #chain.match_ontologies([r.ontology, r1.ontology])
    ##############################
    #testing local HTML template parsing
    r = reader.ontology_reader("owl_rdfxml_parser", "ontologies/cafe-test.owl")
    r1 = reader.ontology_reader("owl_rdfxml_parser", "ontologies/envo-test.owl")
    chain = matching_tool_chain.tool_chain()
    chain.add_config_from_file("./all_matchers-config.xml")
    result = chain.match_ontologies([r.ontology, r1.ontology])
    context = {"title":"Matched Ontologies", "results":result}
    template_raw = util.readFileContentAsString(os.path.dirname(__file__) + "/result_writer/matching_result.html")
    template_content = Template(template_raw)
    util.write2File("matches.html", template_content.render(Context(context)), "w")
    ##############################
    #for testing PyDictionary
    #dictionary = PyDictionary.PyDictionary()
    #print dictionary.synonym("m3u")