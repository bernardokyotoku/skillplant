from django.shortcuts import render_to_response
from django.template import loader,Context
from django.http import HttpResponse
from datetime import datetime
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
	answer.user_answer = int(request.POST['answer'])
	answer.correct = (answer.user_answer == bigger + smaller)
	answer.date_taken = datetime.now()
	answer.save()
	if answer.correct:
		return HttpResponse('correct')
	return HttpResponse('incorrect')
