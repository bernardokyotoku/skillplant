from django.shortcuts import render_to_response
from django.template import loader,Context
from django.http import HttpResponse
from datetime import datetime
import student as stdent
import django.utils.simplejson as json
from addition import engine
from addition.models import AddQuestion, Answer


def get_question(request):
#	student = Student.who_is(request.user)
	student=''
	question = engine.select_question(student)
	return HttpResponse(question.json)

def store_answer_and_return_evaluation(request):
	# store answer
	return HttpResponse(AddQuestion.objects.all())
	question = AddQuestion.objects.get(pk=request.POST['question_key'])
	answer = Answer()
	answer.user = request.user
	answer.question = question
	answer.value = request.POST['answer']
	answer.time_taken = datetime.now() - datetime.now()
	answer.correct = answer.value == answer.question.correct_answer
	answer.save()
	return HttpResponse('correct')
	#return ask(question.select_question(user))


