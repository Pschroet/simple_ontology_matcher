"""
Django settings for MasterThesis project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import sys

import json
import requests
import util

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR + "/OntologyMatcher")
sys.path.append(BASE_DIR + "/OntologyMatcher/reader")
sys.path.append(BASE_DIR + "/OntologyMatcher/matcher")
sys.path.append(BASE_DIR + "/OntologyMatcher/resources")


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'dw%9f1!944*lgzx3u=c@a8dd_-h*j(70-*2n4lciq(n9-fo0vk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

#since there are no own Middleware classes used, set the variable to an empty list
MIDDLEWARE_CLASSES=[]

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'OntologyMatcher.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_ROOT = BASE_DIR + "/OntologyMatcher/static"

STATIC_URL = '/resources/'

STATICFILES_DIRS = [
    BASE_DIR + "/OntologyMatcher/resources/",
]

# set the constants for the ontologies, their URLs and the matchers

#get local ontologies
ONTOLOGIES = {}
TERMINOLOGIES = {}
print "Getting ontologies from disk:"
ONTOLOGIES["onto"] = {"label":"server files", "ontos":[]}
for item in util.get_files_in_directory(os.path.dirname(__file__) + "/ontologies", False):
    ONTOLOGIES["onto"]["ontos"].append([item.split(".")[0], os.path.dirname(__file__) + "/ontologies/" + item])
    print "\t" + item + " found"
try:
    re = requests.get("http://terminologies.gfbio.org/api/terminologies/")
    jo = json.loads(re.text)
    #get available ontology information from http://terminologies.gfbio.org/api/terminologies/
    print "Getting terminologies from http://terminologies.gfbio.org/api/terminologies/"
    ONTOLOGIES["term"] = {"label":"terminologies.gfbio.org", "ontos":[]}
    for item in jo["results"]:
        #check if URL is working
        #print item["acronym"]
        onto = requests.head(item["uri"])
        ONTOLOGIES["term"]["ontos"].append([item["acronym"], "http://terminologies.gfbio.org/api/terminologies/" + item["acronym"]])
        print "\t" + item["acronym"] + " added: " + item["name"] + ", " + "http://terminologies.gfbio.org/api/terminologies/" + item["acronym"]
    #get available ontologies from http://terminologies.gfbio.org/api/terminologies/
    #print "Getting ontologies from http://terminologies.gfbio.org/api/terminologies/"
    #for item in jo["results"]:
    #    #check if URL is working
    #    #print item["acronym"]
    #    onto = requests.head(item["uri"])
    #    #print onto.headers
    #    if ("text/plain" in onto.headers['content-type'] or "text/xml" in onto.headers['content-type']) and 'Content-Length' in onto.headers and int(onto.headers['Content-Length']) < 10000000 and (TERMINOLOGIES[item["acronym"]] is None or TERMINOLOGIES[item["acronym"]] is ""):
    #        ONTOLOGIES[item["acronym"]] = [item["name"], item["uri"]]
    #        print "\t" + item["acronym"] + " added: " + item["name"] + ", " + item["uri"]
    #    else:
    #        print "\t" + item["acronym"] + " not added"
except requests.exceptions.RequestException:
    pass
except requests.exceptions.ConnectionError:
    pass

#get the matchers
print "Getting matchers from disk"
MATCHERS = util.filter_files_from_list(util.get_files_in_directory(os.path.dirname(__file__) + "/matcher", False), "pyc")
print "Found " + str(MATCHERS)
print "finished\n--------------------------------------------------"