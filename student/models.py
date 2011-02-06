from django.contrib.auth.models import User
from djangotoolbox.fields import ListField
from django.db import models

class Student(models.Model):
	user = models.ForeignKey(User) 
	_answer_history = ListField()
	facebook_id = models.TextField()
	open_id = models.TextField()
	orkut_id = models.TextField()
	ms_im_id = models.TextField()
	sample_number = models.IntegerField(5)
	dominated_question_answing_time = models.TimeField(1)
	def who_is(self,user):
		student = self.objects.get(user=user)
		return student
#	def history(self,question):
#		index = int(question.operation[0]) * 100
#		index += (question.second_number - 1) * 10
#		index += question.first_number - 1
#		return self._answer_history[index]
#
#	def dominated(self,question):
#		answers_list = self.history(question)
#		last_answers = answers_list[-1-sample_number:-1]
#		for ans in last_answers:
#			if not ans.is_correct or ans.time_taken >= self.dominated_ans_time:
#				return False
#		return True
#
#	def dominated_second_number(self,question):
#		for i in range(10):
#			question = question.increment_first_number()	
#			if not self.dominated(question):
#				return False	
#		return True
