import sys
from django.shortcuts import render_to_response
from django.template import loader,Context
from django.http import HttpResponse
from datetime import datetime, timedelta
import student as stdent
import django.utils.simplejson as json
from addition import engine
from addition.models import Answer

def get_question(request):
	question = engine.select_question(request.user)
	return HttpResponse(json.dumps(question))

def store_answer_and_return_evaluation(request):
	# store answer
	first = int(request.POST['first'])
	second = int(request.POST['second'])
	bigger = max([first,second])
	smaller = min([first,second])
	answer = Answer()
	answer.user = request.user
	answer.question_id = engine.apSum(bigger) + smaller
	#answer.question = question
	ans = request.POST['answer'];
	if not ans.isdigit():
		ans=0
	answer.user_answer = int(ans)
	answer.correct = (answer.user_answer == bigger + smaller)
	answer.date_taken = datetime.now()
	answer.time_taken = timedelta(seconds=float(request.POST['time']))
	answer.save()
	return get_question(request)
	if answer.correct:
		return HttpResponse('correct')
	return HttpResponse('incorrect')

def dominance_question_data(request):
	dominance_questions = engine.sorted_dominance_question_array(request.user)
	data = dict(zip(('dominance','questions','sdf'),dominance_questions+[tuple(range(1,55)),]))
	return HttpResponse(json.dumps(data))
