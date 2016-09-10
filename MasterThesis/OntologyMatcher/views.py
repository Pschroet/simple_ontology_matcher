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
import re


def index(request):
    if request.method == "GET":
        context = {}
        #show the start page, where the ontologies and matcher can be chosen
        if request.path == "/matcher/":
            ontos = util.get_files_in_directory(os.path.dirname(__file__) + "/ontologies", False)
            matchers = util.filter_files_from_list(util.get_files_in_directory(os.path.dirname(__file__) + "/matcher", False), "pyc")
            print  matchers
            context = {"title":"Ontology Matcher", "ontologies":ontos, "matchers":matchers}
            template_raw = util.readFileContentAsString(os.path.dirname(__file__) + "/index.html")
            template_content = template.Template(template_raw)
        #get the matches and show the result
        elif request.path == "/matcher/result_writer/matching_result.html":
            params = []
            if request.GET.getlist('onto') != []:
                params_onto = request.GET.getlist('onto')
            if request.GET.getlist('matcher') != []:
                params_matcher = request.GET.getlist('matcher')
            ontos = []
            matchers = []
            if params_onto != [] and params_matcher != []:
                for param in params_onto:
                    #check for path wandering
                    if not re.match(".*[.][.].*", param):
                        ontos.append(reader.ontology_reader("owl_rdfxml_parser", "./OntologyMatcher/ontologies/" + param).ontology)
                    else:
                        ontos = []
                for param in params_matcher:
                    #check for path wandering
                    if not re.match(".*[.][.].*", param):
                        matchers.append(param)
                    else:
                        matchers = []
                if ontos != [] and matchers != []:
                    #compare the ontologies
                    chain = matching_tool_chain.tool_chain()
                    #chain.add_config_from_file("./OntologyMatcher/test-config.xml")
                    chain.add_matchers(matchers)
                    result = chain.match_ontologies(ontos)
                    context = {"result":result, "title":"Matched Ontologies"}
                    template_raw = util.readFileContentAsString(os.path.dirname(__file__) + "/result_writer/matching_result.html")
                    template_content = template.Template(template_raw)
        if context != {}:
            return HttpResponse(template_content.render(template.Context(context)))
        template_raw = util.readFileContentAsString(os.path.dirname(__file__) + "/error.html")
        template_content = template.Template(template_raw)
        return HttpResponse(template_content.render(template.Context({"title":"Ontology Matcher"})))