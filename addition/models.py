from student.models import Student
from django.db import models
from datetime import date
import django.utils.simplejson as json

class AddQuestion(models.Model):
	first = models.IntegerField()
	second = models.IntegerField()
	correct_result = models.IntegerField()
	@property
	def json(self):
		question = {
			'first':self.first,
			'second':self.second,
			'key':self.pk
			}
		return json.dumps(question)
	def __init__(self,first,second):
		models.Model.__init__(self)
		self.first = first
		self.second = second
		self.correct_result = first + second
	def __unicode__(self):
		return str(self.first)+'+'+str(self.second)+'= '

class Answer(models.Model):
	student = models.ForeignKey(Student)
	question = models.ForeignKey(AddQuestion)
	user_answer = models.IntegerField()
	time_taken = models.TimeField()
	date_taken = models.DateTimeField()
	def __init__(self,answer=None,time_taken=None,date_taken=date.today()):
		self.parent.__init__()
		self.user_answer = answer
		self.time_taken = time_taken
		self.date_taken = date_taken	

	def __unicode__(self):
		return str(self.question)+str(self.user_answer)

