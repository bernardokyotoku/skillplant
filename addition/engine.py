from addition.models import Answer
import math
			
def generateAllQuestions():
	for i in range(1,11):
		for j in range(1,i+1):
			question = AddQuestion()
			question.first = i
			question.second = j
			question.correct_answer = i+j
			print question
	return
			
def select_question(user):
	dominance = get_dominance_for(user)
	dom = map(dominance,range(1,55))
	hmd = max(dom)/2
	domi = [(dom[i-1],i) for i in range(1,55)] 
	domi.sort()
	sor_do = [i[0]<hmd for i in domi]
	if True not in sor_do:
		halfMaxCrossIndex = 0
	else:
		halfMaxCrossIndex = sor_do.index(True) 
	index = raffle(halfMaxCrossIndex,4)
	selected_question = domi[index][1]
	question =  naturalLearningOrder(selected_question)
	qdict = {'first':question[0],'second':question[1]}
	return qdict

def raffle(center,width):
	import random
	return abs(int(random.gauss(center,width)))

def get_dominance_for(user):
	return lambda question : dominance(question,user)
	
def naturalLearningOrder(num):
	i = revSum(num)
	return (i,num-apSum(i-1))

def apSum(m):
	return m*(m+1)/2

def revSum(n):
	return int(math.ceil((math.sqrt(1+8*n)-1)/2))

def dominance(q_id,user):
	answers = Answer.objects.filter(user=user)	
	answers = answers.filter(question_id=q_id)
	if len(answers) is 0:
		return 0
	return 1/average_time(answers)
	
def average_time(answers):
	if len(answers) > 4:
		answers.order_by('date_taken')
		last_answers = answers.reverse()[:5]
	else:
		last_answers = answers
	time = []
	for answer in last_answers:
		time += [answer.time_taken.second]
	return sum(time)/len(time)
