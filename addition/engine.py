from addition.models import AddQuestion

def select_question(student):
	question = AddQuestion(3,4)
	question.save()
	return question 
			
