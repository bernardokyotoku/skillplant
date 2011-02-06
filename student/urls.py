from django.conf.urls.defaults import *

urlpatterns = patterns('student',
	('^$','views.show_student_homepage'),
)
