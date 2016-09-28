'''
Created on 04.09.2016

@author: Philipp Schroeter
'''

from django import template
from django.http import HttpResponse
from django.http import FileResponse
import matching_tool_chain
import reader
import util
import os
import re
from django.views.decorators.csrf import csrf_exempt
import urlparse

@csrf_exempt
def index(request):
    if request.method == "GET" or request.method == "POST":
        context = {}
        #get the matches and show the result
        if request.path == "/resources/scripts.js":
            return FileResponse(util.readFileContentAsString("resources/scripts.js"))
        elif request.path == "/matcher/result_writer/matching_result.html":
            params_onto = []
            params_matcher = []
            if request.GET.getlist('Onto') != []:
                params_onto = request.GET.getlist('Onto')
            if request.GET.getlist('Matcher') != []:
                params_matcher = request.GET.getlist('Matcher')
            ontos = []
            matchers = []
            available_ontologies = util.get_ontologies()
            if params_onto != [] and params_matcher != []:
                for param in params_onto:
                    source = available_ontologies[param][1]
                    #print urlparse.urlparse(available_ontologies[param][1]).scheme
                    if bool(urlparse.urlparse(source).scheme):
                        tmp = reader.ontology_reader("owl_rdfxml_web_parser", source).ontology
                        #print tmp.tostring()
                        ontos.append(tmp)
                    elif os.path.isfile(source):
                        tmp = reader.ontology_reader("owl_rdfxml_parser", source).ontology
                        #print tmp.tostring()
                        ontos.append(tmp)
                for param in params_matcher:
                    #check for path wandering
                    if not re.match(".*[.][.].*", param):
                        matchers.append(param)
                    else:
                        matchers = []
                        break
                if ontos != [] and matchers != []:
                    #compare the ontologies
                    chain = matching_tool_chain.tool_chain()
                    #chain.add_config_from_file("./OntologyMatcher/all_matchers-config.xml")
                    chain.add_matchers(matchers)
                    result = chain.match_ontologies(ontos)
                    context = {"title":"Matched Ontologies", "results":result}
                    template_raw = util.readFileContentAsString(os.path.dirname(__file__) + "/result_writer/matching_result.html")
                    template_content = template.Template(template_raw)
        #show the start page, where the ontologies and matcher can be chosen
        elif request.path == "/matcher/":
            ontos = util.get_ontologies()
            matchers = util.get_matchers()
            context = {"title":"Ontology Matcher", "ontologies":ontos, "matchers":matchers}
            template_raw = util.readFileContentAsString(os.path.dirname(__file__) + "/index.html")
            template_content = template.Template(template_raw)
        if context != {}:
            return HttpResponse(template_content.render(template.Context(context)))
        template_raw = util.readFileContentAsString(os.path.dirname(__file__) + "/error.html")
        template_content = template.Template(template_raw)
        return HttpResponse(template_content.render(template.Context({"title":"Ontology Matcher"})))