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
            #get the passed ontologies
            available_ontologies = util.get_ontologies()
            params_onto = []
            params_matcher = []
            #look for each kind of source, if there are ontologies passed from this type
            for ontology in available_ontologies:
                if request.GET.getlist(ontology) != []:
                    passed_arguments = request.GET.getlist(ontology)
                    #get the exact source information from the type of ontology
                    for ontology_type in available_ontologies[ontology]["ontos"]:
                        if ontology_type[0] in passed_arguments:
                            params_onto.append(ontology_type[1])
            #get the passed matchers
            if request.GET.getlist('Matcher') != []:
                params_matcher = request.GET.getlist('Matcher')
            ontos = []
            matchers = []
            if params_onto is not [] and (params_matcher is not []):
                for source in params_onto:
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
                        matchers.append(param.replace(".py", ""))
                    else:
                        matchers = []
                        break
                if ontos is not [] and matchers is not []:
                    #compare the ontologies
                    chain = matching_tool_chain.tool_chain()
                    chain.set_matchers(matchers)
                    result = chain.match_ontologies(ontos)
                    connection_options = ["None", "owl:sameAs", "rdfs:subClassOf", "dcterms:partOf", "dcterms:hasPart", "rdfs:subPropertyOf", "owl:equivalentClass", "owl:intersectionOf", "owl:differentFrom", "owl:disjointWith", "owl:inverseOf"]
                    context = RequestContext(request, {"title":"Matched Ontologies", "results":result, "connection_options":connection_options, "ontologies":ontos})
                    template_raw = util.readFileContentAsString(os.path.dirname(__file__) + "/result_writer/matching_result.html")
                    template_content = template.Template(template_raw)
        #show the start page, where the ontologies and matcher can be chosen
        elif request.path == "/matcher/":
            ontos = util.get_ontologies()
            matchers = util.get_matchers()
            context = RequestContext(request, {"title":"Ontology Matcher", "ontologies":ontos, "matchers":matchers})
            template_raw = util.readFileContentAsString(os.path.dirname(__file__) + "/index.html")
            template_content = template.Template(template_raw)
        if context != {}:
            return HttpResponse(template_content.render(RequestContext(request, context)))
        template_raw = util.readFileContentAsString(os.path.dirname(__file__) + "/error.html")
        template_content = template.Template(template_raw)
        return HttpResponse(template_content.render(RequestContext(request, {"title":"Ontology Matcher"})))