from django.conf.urls.defaults import *

urlpatterns = patterns('game.views',
	('^question/(?P<op>.+)$','question'),
)
