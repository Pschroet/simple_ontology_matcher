'''
Created on 13.08.2016

@author: Philipp Schroeter
'''

import matching_tool_chain
import reader
import util
import os
from django.conf import settings
from django.template import Context, Template
from django.template.engine import Engine
import PyDictionary
import xmlrdf_reader
import compare_matchings

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
    #r = reader.ontology_reader("owl_rdfxml_parser", "ontologies/cafe-test.owl")
    #r1 = reader.ontology_reader("owl_rdfxml_parser", "ontologies/envo-test.owl")
    #chain = matching_tool_chain.tool_chain()
    #chain.add_config_from_file("./all_matchers-config.xml")
    #result = chain.match_ontologies([r.ontology, r1.ontology])
    #settings.configure(DEBUG=False)
    #context = {"title":"Matched Ontologies", "results":result}
    #template_raw = util.readFileContentAsString(os.path.dirname(__file__) + "/result_writer/matching_result.html")
    #template_content = Template(template_raw, engine=Engine())
    #util.write2File("matches.html", template_content.render(Context(context)), "w")
    ##############################
    #for testing PyDictionary
    #dictionary = PyDictionary.PyDictionary()
    #print dictionary.synonym("test")
    #print dictionary.synonym("search")
    ##############################
    #for checking the results of the matchers
    matching = xmlrdf_reader.parse_matchings_file("./additional_modules/matches-1.rdf")
    matching1 = xmlrdf_reader.parse_matchings_file("./additional_modules/envo_pato.rdf")
    result = compare_matchings.compare(matching, matching1)
    settings.configure(DEBUG=False)
    context = {"title":"Matching Comparison", "same":result[0], "different":result[1]}
    template_raw = util.readFileContentAsString(os.path.dirname(__file__) + "./additional_modules/matching_comparison.html")
    template_content = Template(template_raw, engine=Engine())
    util.write2File("matching_comparison.html", template_content.render(Context(context)), "w")