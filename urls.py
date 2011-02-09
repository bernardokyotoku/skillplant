from django.conf.urls.defaults import *

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
	('^_ah/warmup$', 'djangoappengine.views.warmup'),
#	('^game/',include('game.urls')),
	('^addition/', include('addition.urls')),
	('^socialauth/', include('socialauth.urls')),
	('^student/$',include('student.urls')),
	('^addition$',include('addition.urls')),
)
