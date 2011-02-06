from django.conf.urls.defaults import *
urlpatterns = patterns('login.views',
	('^$', 'login'),
	('^host$', 'host'),
	('^\?', 'login'),
	('^/logout$','logout'),
)
