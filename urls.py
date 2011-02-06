from django.conf.urls.defaults import *

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
	('^_ah/warmup$', 'djangoappengine.views.warmup'),
#	('^game/',include('game.urls')),
	('^addition/', include('addition.urls')),
	('^login/', include('login.urls')),
	('^student/$',include('student.urls')),
	('^addition$',include('addition.urls')),
)
