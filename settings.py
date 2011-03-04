# Initialize App Engine and import the default settings (DB backend, etc.).
# If you want to use a different backend you have to remove all occurences
# of "djangoappengine" from this file.
try:
    from djangoappengine.settings_base import *
    has_djangoappengine = True
except ImportError:
    has_djangoappengine = False
    DEBUG = True
    TEMPLATE_DEBUG = DEBUG

import os

#DATABASE_ENGINE = 'sqlite3'  
#DATABASE_NAME = 'Users/bernardo/Project/skillplant/db/data'             
#DATABASE_USER = ''             # Not used with sqlite3.
#DATABASE_PASSWORD = ''         # Not used with sqlite3.
#DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
#DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Uncomment the following if you want to use MongoDB
# -----------------
#DATABASES = {
#    'default': {
#        'ENGINE': 'django_mongodb_engine.mongodb',
#        'NAME': 'test',
#        'USER': '',
#        'PASSWORD': '',
#        'HOST': 'localhost',
#        'PORT': 27017,
#        'SUPPORTS_TRANSACTIONS': False,
#    }
#}
# -----------------

SITE_NAME = ''
SITE_DESCRIPTION = ''
SITE_COPYRIGHT = ''
DISQUS_SHORTNAME = ''
GOOGLE_ANALYTICS_ID = ''
# Get the ID from the CSE "Basics" control panel ("Search engine unique ID")
GOOGLE_CUSTOM_SEARCH_ID = ''
# Set RT username for retweet buttons
TWITTER_USERNAME = ''
# In order to always have uniform URLs in retweets and FeedBurner we redirect
# any access to URLs that are not in ALLOWED_DOMAINS to the first allowed
# domain. You can have additional domains for testing.
ALLOWED_DOMAINS = ()

SECRET_KEY = '=r-$b*8hglm+858&9t043hlm6-&6-3d3vfc4((7yd0dbrakhvi'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.contenttypes',
    'django.contrib.sitemaps',
    'djangotoolbox',
	'socialauth',
	'openid_consumer',
	'addition',
)

if has_djangoappengine:
    # djangoappengine should come last, so it can override a few manage.py commands
    INSTALLED_APPS += ('djangoappengine',)

# This test runner captures stdout and associates tracebacks with their
# corresponding output. Helps a lot with print-debugging.
TEST_RUNNER = 'djangotoolbox.test.CapturingTestSuiteRunner'







MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
 	'djangotoolbox.middleware.RedirectMiddleware',
	'google.appengine.ext.appstats.recording.AppStatsDjangoMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
    'openid_consumer.middleware.OpenIDMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',   
)







TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    "socialauth.context_processors.facebook_api_key",

)


TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), 'templates'),)



























ADMIN_MEDIA_PREFIX = '/media/admin/'

ROOT_URLCONF = 'urls'

NON_REDIRECTED_PATHS = ('/admin/',)


## Activate django-dbindexer if available
try:
    import dbindexer
    DATABASES['native'] = DATABASES['default']
    DATABASES['default'] = {'ENGINE': 'dbindexer', 'TARGET': 'native'}
    INSTALLED_APPS += ('dbindexer',)
    DBINDEXER_SITECONF = 'dbindexes'
    MIDDLEWARE_CLASSES = ('dbindexer.middleware.DBIndexerMiddleware',) + \
                         MIDDLEWARE_CLASSES
except ImportError:
    pass

try:
    from localsettings import *
except ImportError:
    pass

LOGIN_REDIRECT_URL = '/static/question.html'
LOGOUT_REDIRECT_URL = '/'

#SITE_ID = 29
