from django.contrib import auth
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template import Template, Context

import cgi
import urllib2
import urllib
from login import models
from login import settings

def loginBernardo(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/student/')
	try:
		user = auth.models.User.objects.get(first_name='Bernardo')
	except auth.models.User.DoesNotExist:
		user = auth.models.User()
		user.first_name = 'Bernardo'
		
	if user.is_active:
			auth.login(request, user)
				return HttpResponseRedirect('/student/')
			else:
				error = 'AUTH_DISABLED'
		else:
			error = 'AUTH_FAILED'
		
def host(request):
	
	if request.user.is_authenticated():
		return HttpResponseRedirect('/student')

	if not request.POST:
		template_context = {'settings': settings, 'error': error}
		context_instance = RequestContext(request)
		return render_to_response('login.html', template_context, context_instance)
	
	username = request.POST['user']
	password = request.POST['pass']	
	user = auth.authenticate(username,password)
	if user:
		if user.is_active:
			auth.login(request, user)
			return HttpResponseRedirect('/student')
		else:
			error = 'AUTH_DISABLED'
	else:
		error = 'AUTH_FAILED'
		

def facebook(request):
	error = None

	if request.user.is_authenticated():
		return HttpResponseRedirect('/student/')

	if request.GET:
		if 'code' in request.GET:
			args = {
				'client_id': settings.FACEBOOK_APP_ID,
				'redirect_uri': settings.FACEBOOK_REDIRECT_URI,
				'client_secret': settings.FACEBOOK_API_SECRET,
				'code': request.GET['code'],
			}

			url = 'https://graph.facebook.com/oauth/access_token?' + \
					urllib.urlencode(args)
			risposta = urllib2.urlopen(url).read()
			response = cgi.parse_qs(risposta)
			access_token = response['access_token'][0]
			expires = response['expires'][0]

			facebook_session = models.FacebookSession.objects.get_or_create(
				access_token=access_token,
			)[0]

			facebook_session.expires = expires
			facebook_session.save()
			user = auth.authenticate(token=access_token)
			if user:
				if user.is_active:
					auth.login(request, user)
					return HttpResponseRedirect('/student/')
				else:
					error = 'AUTH_DISABLED'
			else:
				error = 'AUTH_FAILED'
		elif 'error_reason' in request.GET:
			error = 'AUTH_DENIED'

	template_context = {'settings': settings, 'error': error}
	return render_to_response('login.html', template_context, context_instance=RequestContext(request))


def logout(request):
	auth.logout(request)
	return HttpResponse('Logged out, bye!')

