from djangotoolbox.fields import ListField
from django.db import models
from student.models import Student
from random import random

OPERATION_CHOICES = (
	('0',u'addition'),
	('1',u'subtraction'),
	('2',u'multiplication'),
	('3',u'division'),
)

ASK_CHANCE = 0.1

def ask_anyway():
	return random < ASK_CHANCE

class Question(models.Model):
	first_number = models.IntegerField()
	second_number = models.IntegerField()
	operation = models.TextField(choices=OPERATION_CHOICES)
	def get(self,first,second,op):
		return self.objects.get(first_number=first,second_number=second,operation=op)
#	def __init__(self,first,second):
#		self.first_number = first
#		self.second_number = second
	def increment_first_number(self):
		num = self.first_number % 10 + 1
		return self.get(num,self.second_number,self.operation)
	def increment_second_number(self):
		num = self.second_number % 10 + 1
		return self.get(self.first_number,num,self.operation)
	def select_question(self,student):
		if student.dominated_second_number(self):
			question = change_both_numbers(self,student)
		else:
			question = change_first_number(self,student)
		play(question)
	def change_first_number(self,student):
		question = self
		while True:
			question = question.increment_first_number()
			if not student.dominated(question,operation) or ask_anyway():
				return question
	def change_both_numbers(self,student):
		while True:
			question = question.increment_second_number()
			if not student.dominated(question,operation) or ask_anyway():
				return change_first_number(question,student) 

class Answer(models.Model):
	student = models.ForeignKey(Student)
	question = models.ForeignKey(Question)
	answer = models.IntegerField()
	answered_correct = models.BooleanField()
	datetime = models.DateTimeField()
	time_taken = models.TimeField()
	def save(self):
		super.save()
		self.student._answer_list += self.pk
		self.student.save()	

class AnswerHistory(models.Model):
	student = models.ForeignKey(Student)
	question = models.ForeignKey(Question)
	_answer_list = ListField()
	@property
	def list(self):
		ans_list = []
		for ans in self._answer_list:
			ans_list += Answer.objects.get(pk=ans)
		return ans_list
