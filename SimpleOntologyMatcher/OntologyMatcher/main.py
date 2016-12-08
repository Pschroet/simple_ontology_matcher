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
    #chain.add_config_from_file("./all_matchers-config.xml")
    #chain.match_ontologies([r.ontology, r1.ontology])
    ##############################
    #testing local HTML template parsing
    r = reader.ontology_reader("owl_rdfxml_parser", "ontologies/pato.owl")
    r1 = reader.ontology_reader("owl_rdfxml_parser", "ontologies/envo.owl")
    #testing the terminology server
    #r = reader.ontology_reader("GFBio_terminology_server_parser", "http://terminologies.gfbio.org/api/terminologies/ENVO")
    #print r.ontology.tostring()
    #r1 = reader.ontology_reader("GFBio_terminology_server_parser", "http://terminologies.gfbio.org/api/terminologies/PATO")
    #print r1.ontology.tostring()
    chain = matching_tool_chain.tool_chain()
    chain.add_config_from_file("./all_matchers-config.xml")
    result = chain.match_ontologies([r.ontology, r1.ontology])
    settings.configure(DEBUG=False)
    context = {"title":"Matched Ontologies", "results":result}
    template_raw = util.readFileContentAsString(os.path.dirname(__file__) + "/result_writer/matching_result.html")
    template_content = Template(template_raw, engine=Engine())
    util.write2File("matches.html", template_content.render(Context(context)), "w")
    ##############################
    #for testing PyDictionary
    #dictionary = PyDictionary.PyDictionary()
    #print dictionary.synonym("test")
    #print dictionary.synonym("search")
    ##############################
    #for checking the results of the matchers
    #matching = xmlrdf_reader.parse_matchings_file("./additional_modules/matches-3.rdf")
    #print len(matching)
    #matching1 = xmlrdf_reader.parse_matchings_file("./additional_modules/envo_pato.rdf")
    #print len(matching1)
    #result = compare_matchings.compare(matching, matching1)
    #print result
    #settings.configure(DEBUG=False)
    #context = {"title":"Matching Comparison", "same":result[0], "different":result[1], "different_names":["matches-3.rdf", "envo_pato.rdf"]}
    #template_raw = util.readFileContentAsString(os.path.dirname(__file__) + "./additional_modules/matching_comparison.html")
    #template_content = Template(template_raw, engine=Engine())
    #util.write2File("matching_comparison.html", template_content.render(Context(context)), "w")
    #test: matching PANGAEA and EASE
    #r = reader.ontology_reader("rdf_xml_parser", "ontologies/PANGAEA.rdf")
    ##print r.ontology.tostring()
    #r1 = reader.ontology_reader("owl_rdfxml_parser", "ontologies/ease.owl")
    #chain = matching_tool_chain.tool_chain()
    #chain.add_config_from_file("./all_matchers-config.xml")
    #result = chain.match_ontologies([r.ontology, r1.ontology])
    #settings.configure(DEBUG=False)
    #context = {"title":"Matched Ontologies", "results":result}
    #template_raw = util.readFileContentAsString(os.path.dirname(__file__) + "/result_writer/matching_result.html")
    #template_content = Template(template_raw, engine=Engine())
    #util.write2File("matches.html", template_content.render(Context(context)), "w")