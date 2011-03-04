from student.models import Student
from django.db import models
from datetime import date
import django.utils.simplejson as json
from django.contrib.auth.models import User

from addition.settings import *

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
	time_taken = models.TimeField()
	date_taken = models.DateTimeField()
	correct = models.BooleanField()
	dominance_relevant = models.BooleanField()
	def save(self, *args, **kwargs):
		answers_query = Answer.objects.filter(	user = self.user,
										question_id = self.question_id,
										dominance_relevant = True)
		answers_query.order_by('date_taken')
		answers = list(answers_query)
		if NUMBER_RELEVANT_ANSWERS <= len(answers):
			answers.reverse()
			oldest_relevent_answer = answers[0]
			oldest_relevent_answer.dominance_relevant = False
		self.dominance_relevant = True
		super(Answer, self).save(*args, **kwargs)
