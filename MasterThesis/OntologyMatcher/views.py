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
    if request.method == "GET":
        context = {}
        if request.path == "/matcher/":
            ontos = util.get_files_in_directory(os.path.dirname(__file__) + "/ontologies", False)
            context = {"ontologies":ontos, "title":"Ontology Matcher"}
            template_raw = util.readFileContentAsString(os.path.dirname(__file__) + "/index.html")
            template_content = template.Template(template_raw)
        elif request.path == "/matcher/result_writer/matching_result.html":
            params = []
            if request.GET.getlist('onto') != []:
                params = request.GET.getlist('onto')
            ontos = []
            if params != []:
                for param in params:
                    ontos.append(reader.ontology_reader("owl_rdfxml_parser", "./OntologyMatcher/ontologies/" + param).ontology)
                if ontos != []:
                    #compare the ontologies
                    chain = matching_tool_chain.tool_chain("./OntologyMatcher/test-config.xml")
                    result = chain.match_ontologies(ontos)
                    context = {"result":result, "title":"Matched Ontologies"}
                    template_raw = util.readFileContentAsString(os.path.dirname(__file__) + "/result_writer/matching_result.html")
                    template_content = template.Template(template_raw)
        if context != {}:
            return HttpResponse(template_content.render(template.Context(context)))