from student.models import Student 
from login.models import FacebookSession
from django.template import loader,Context
from django.template.loader import render_to_string
from django.http import HttpResponse

def show_student_homepage(request):
	#check if user is authenticated
	#and if he has permission to see this page
	#user = User.objects.get(username=request.user.username)
	#profile = Profile.objects(get request.user)[0]
	template = loader.get_template('student_homepage_template.html')
	#return HttpResponse(' <html>here %s</html>'%request.user.username)
	a = template.render(Context({ 'user' : request.user}))
	#a = render_to_string('student_homepage_template.html',{'user':'dfs'})
	return HttpResponse(a)
