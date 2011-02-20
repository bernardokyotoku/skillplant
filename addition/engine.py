from addition.models import AddQuestion

def select_question(user):
	question = AddQuestion.objects.get(first=3,second=4)
	return question 
			
def generateAllQuestions():
	for i in range(1,11):
		for j in range(1,11):
			question = AddQuestion()
			question.first = i
			question.second = j
			question.correct_answer = i+j
			question.save()
	return


#def dominance(question,user):
#	try:
#	ans = Answer.objects.filter(question=question,user=user)	
#	except NoSuchElement:
#		return 0
#	return 1/average_time(answer)	
#	
#def average_time(answer):
#	if len(ans) > 4:
#		last_ans = ans[-5,-1]
#	else:
#		last_ans = ans
#	time = []
#	for answer = last_answers:
#		time += [answer.time_taken]
#	return sum(time)/len(time)
