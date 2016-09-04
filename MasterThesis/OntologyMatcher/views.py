'''
Created on 04.09.2016

@author: Philipp Schroeter
'''

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")