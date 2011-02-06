from django.conf.urls.defaults import *

urlpatterns = patterns('addition.views',
	(r'^get_question$', 'get_question'),
	(r'^post_answer$', 'store_answer_and_return_evaluation'),
)
