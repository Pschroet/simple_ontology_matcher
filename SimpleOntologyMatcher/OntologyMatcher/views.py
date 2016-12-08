'''
Created on 04.09.2016

@author: Philipp Schroeter
'''

from django import template
from django.http import HttpResponse
from django.http import FileResponse
from django.template import RequestContext
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
            params_term = []
            params_matcher = []
            if request.GET.getlist('Onto') != []:
                params_onto = request.GET.getlist('Onto')
            if request.GET.getlist('Term') != []:
                params_term = request.GET.getlist('Term')
            if request.GET.getlist('Matcher') != []:
                params_matcher = request.GET.getlist('Matcher')
            ontos = []
            matchers = []
            available_ontologies = util.combine_dicts(util.get_ontologies(), util.get_terminologies())
            if params_onto is not [] and (params_matcher is not [] or params_term is not []):
                for param in params_onto + params_term:
                    source = available_ontologies[param][1]
                    if bool(urlparse.urlparse(source).scheme) and "terminologies.gfbio.org" in source:
                        tmp = reader.ontology_reader("GFBio_terminology_server_parser", source).ontology
                        #print tmp.tostring()
                        ontos.append(tmp)
                    elif os.path.isfile(source) and re.match(os.path.basename(source).split(".")[1], "owl", re.IGNORECASE):
                        tmp = reader.ontology_reader("owl_rdfxml_parser", source).ontology
                        #print tmp.tostring()
                        ontos.append(tmp)
                    elif os.path.isfile(source) and re.match(os.path.basename(source).split(".")[1], "rdf", re.IGNORECASE):
                        tmp = reader.ontology_reader("rdf_xml_parser", source).ontology
                        #print tmp.tostring()
                        ontos.append(tmp)
                    elif bool(urlparse.urlparse(source).scheme):
                        tmp = reader.ontology_reader("owl_rdfxml_web_parser", source).ontology
                        #print tmp.tostring()
                        ontos.append(tmp)
                for param in params_matcher:
                    #check for path wandering
                    if not re.match(".*[.][.].*", param):
                        matchers.append(param)
                    else:
                        matchers = []
                        break
                if ontos is not [] and matchers is not []:
                    #compare the ontologies
                    chain = matching_tool_chain.tool_chain()
                    #chain.add_config_from_file("./OntologyMatcher/all_matchers-config.xml")
                    chain.add_matchers(matchers)
                    result = chain.match_ontologies(ontos)
                    connection_options = ["None", "rdfs:subClassOf", "owl:equivalentClass", "owl:intersectionOf", "owl:differentFrom", "owl:disjointWith", "owl:inverseOf"]
                    context = RequestContext(request, {"title":"Matched Ontologies", "results":result, "connection_options":connection_options, "ontologies":ontos})
                    template_raw = util.readFileContentAsString(os.path.dirname(__file__) + "/result_writer/matching_result.html")
                    template_content = template.Template(template_raw)
        #show the start page, where the ontologies and matcher can be chosen
        elif request.path == "/matcher/":
            ontos = util.get_ontologies()
            terms = util.get_terminologies()
            matchers = util.get_matchers()
            context = RequestContext(request, {"title":"Ontology Matcher", "ontologies":ontos, "terminologies":terms, "matchers":matchers})
            template_raw = util.readFileContentAsString(os.path.dirname(__file__) + "/index.html")
            template_content = template.Template(template_raw)
        if context != {}:
            return HttpResponse(template_content.render(RequestContext(request, context)))
        template_raw = util.readFileContentAsString(os.path.dirname(__file__) + "/error.html")
        template_content = template.Template(template_raw)
        return HttpResponse(template_content.render(RequestContext(request, {"title":"Ontology Matcher"})))