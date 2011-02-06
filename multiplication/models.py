from django.db import models
from student.models import Student
import game

class Question(game.models.Question):
	class Meta:
		abstract
	def __init__(self,first,second):
		self.first_number = first
		self.second_number = second
	def first_number_incremented(self):
		num = self.first_number % 10 + 1
		return self.objects.get(first_number=num)[0]
	def second_number_incremented(self):
		num = self.second_number % 10 + 1
		return self.objects.get(second_number=num)[0]
	def select_question(self,student):
		if student.dominated_second_number(last_question):
			question = change_both_numbers(last_question,student)
		else:
			question = change_first_number(last_question,student)
		play(question)

	def change_first_number(self,student):
		question = self
		while True:
			question = question.first_number_incremented()
			if not student.dominated(question,operation) or rolled(question):
				return question

	def change_both_numbers(self,student):
		while True
			question = question.second_number_incremented()
			if not student.dominated(question,operation) or rolled(question):
				return change_first_number(question,student) 



class Answer(models.Model):
	student = models.ForeignKey(Student)
	question = models.ForeignKey(Question)
	answer = models.IntegerField()
	answered_correct = models.Boolean()
	date = models.date()
	time_taken = model.time()
	class Meta:
		abstract

class Last_time_mean(models.Model):
	question = models.ForeignKey(Question)
	value = model.FloatField(1E10)


