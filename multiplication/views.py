from multiplication.models import *
from django.template import loader

def ask(question)
	temp = loader.get_template('multiplication_question_template.html')
	context = Context({'question': question })
	return render_to_response(temp.render(context))

def answer(request,question):
	history = History.objects.get(user=request.user)
	history.multiplication.answers
	Answers
	request.POST['answer']

def select_question(last_question,student):
	if student.dominated(last_question) and student.dominated(last_question.second_number):
		question = change_both_numbers(last_question,student)
	else:
		question = change_first_number(last_question,student)
	play(question)

def change_first_number(question,student):
	while True:
		question = question.first_number_incremented()
		if not student.dominated(question) or rolled(question):
			return question

def change_both_numbers(question,student):
	while True
		question = question.second_number_incremented()
		if not student.dominated(question) or rolled(question):
			return change_first_number(question,student) 

