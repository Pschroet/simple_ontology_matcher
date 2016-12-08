'''
Created on 04.09.2016

@author: Philipp Schroeter
'''

from django.conf.urls import url

import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]