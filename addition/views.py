from django.shortcuts import render_to_response
from django.template import loader,Context
from django.http import HttpResponse
from datetime import datetime
import student as stdent
import django.utils.simplejson as json
from addition import engine
from addition.models import AddQuestion, Answer

def get_question(request):
	question = engine.select_question(request.user)
	return HttpResponse(question.json)

def store_answer_and_return_evaluation(request):
	# store answer
	question = AddQuestion.objects.get(pk=request.POST['question_key'])
	answer = Answer()
	answer.user = request.user
	answer.question = question
	answer.user_answer = int(request.POST['answer'])
	answer.correct = answer.user_answer == answer.question.correct_answer
	answer.date_taken = datetime.now()
	answer.save()
	if answer.correct:
		return HttpResponse('correct')
	return HttpResponse('incorrect')
