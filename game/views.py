from django.shortcuts import render_to_response
from django.template import loader,Context
from django.http import HttpResponse
from datetime import datetime
import student as stdent
import game
import django.utils.simplejson as json

def question(request,op):
	q = dict()
	q['first'] = '3'
	q['second'] = '4'
	q['question_key'] = question.pk
	return HttpResponse(json.dumps(q))

def ask(request):
	temp = loader.get_template('question.svg')
	#context = Context({'question': question })
	return render_to_response(temp.render(Context({})))

def store_answer_and_ask_new_question(request):
	# store answer
	student = stdent.models.Student.objects.get(user=request.user)
	question = game.models.Question.objects.get(pk=request.POST['question_key'])
	answer = game.models.Answer()
	answer.student = student
	answer.question = question
	answer.value = request.POST['answer']
	answer.time_taken = datetime.now() - datetime.now()
	answer.correct = answer.value == answer.question.correct_answer
	answer.save()
	return ask(question.select_question(student))


