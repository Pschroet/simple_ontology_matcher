'''
Created on 04.09.2016

@author: Philipp Schroeter
'''

from django import template
from django.http import HttpResponse
import matching_tool_chain
import reader
import util
import os


def index(request):
    #compare the ontologies
    r = reader.ontology_reader("owl_rdfxml_parser", "./OntologyMatcher/cafe.owl")
    r1 = reader.ontology_reader("owl_rdfxml_parser", "./OntologyMatcher/envo.owl")
    chain = matching_tool_chain.tool_chain("./OntologyMatcher/test-config.xml")
    result = chain.match_ontologies([r.ontology, r1.ontology])
    context = {"result":result, "title":"Ontology Matcher"}
    template_raw = util.readFileContentAsString(os.path.dirname(__file__) + "/index.html")
    template_content = template.Template(template_raw)
    template_content.render(template.Context(context))
    return HttpResponse(template_content.render(template.Context(context)))