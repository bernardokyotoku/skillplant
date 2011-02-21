from student.models import Student
from django.db import models
from datetime import date
import django.utils.simplejson as json
from django.contrib.auth.models import User

class AddQuestion(models.Model):
	first = models.IntegerField()
	second = models.IntegerField()
	correct_answer = models.IntegerField()
	@property
	def json(self):
		question = {
			'first':self.first,
			'second':self.second,
			'key':self.pk
			}
		return json.dumps(question)
	def __unicode__(self):
		return str(self.first)+'+'+str(self.second)+'= '

class Answer(models.Model):
	user = models.ForeignKey(User)
	#question = models.ForeignKey(AddQuestion)
	question_id = models.IntegerField()
	user_answer = models.IntegerField()
	#time_taken = models.TimeField()
	date_taken = models.DateTimeField()
	correct = models.BooleanField()
	def __unicode__(self):
		return str(self.question)+str(self.user_answer)

