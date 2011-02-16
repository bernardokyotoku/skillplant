from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
	('^_ah/warmup$', 'djangoappengine.views.warmup'),
#	('^game/',include('game.urls')),
	('^$', 'login.log'),
	('^addition/', include('addition.urls')),
	('^admin/', include(admin.site.urls)),
	('^socialauth/', include('socialauth.urls')),
	('^student/$',include('student.urls')),
	('^addition$',include('addition.urls')),
)
