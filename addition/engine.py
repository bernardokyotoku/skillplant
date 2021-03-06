from addition.models import Answer
import math
import sys
			
def select_question(user):
	dominance,questions = sorted_dominance_question_array(user)
	hmd = max(dominance)/2
	sor_do = map(lambda i:i<hmd,dominance)
	if True not in sor_do:
		halfMaxCrossIndex = 0
	else:
		halfMaxCrossIndex = sor_do.index(True) 
	index = raffle(halfMaxCrossIndex,4)
	selected_question = questions[index]
	question =  naturalLearningOrder(selected_question)
	qdict = {'first':question[0],'second':question[1]}
	return qdict

def sorted_dominance_question_array(user):
	question = range(1,55)
	dominance = map(get_dominance_for(user),question)
	return sort_array((dominance,question))

def transpose(arg):
	return zip(*arg)

def sort_array(arg):
	arg = [arg[0],map(lambda x:-x,arg[1])]
	a = transpose(arg)
	a.sort()
	a.reverse()
	a = transpose(a)
	a = [a[0],map(lambda x:-x,a[1])]
	return a

def raffle(center,width):
	import random
	return abs(int(random.gauss(center,width)))

def get_dominance_for(user):
	answers_query = Answer.objects.filter(user=user,dominance_relevant=True)
	answers = list(answers_query)
	return lambda q_id : dominance(q_id,answers)
	
def dominance(q_id,answers):
	q_ans = filter(lambda ans:ans.question_id == q_id,answers)	
	if len(q_ans) is 0:
		return 0
	return 1/average_time(q_ans)

def naturalLearningOrder(num):
	i = revSum(num)
	return (i,num-apSum(i-1))

def apSum(m):
	return m*(m+1)/2

def revSum(n):
	return int(math.ceil((math.sqrt(1+8*n)-1)/2))

def average_time(answers):
	time = []
	for answer in answers:
		time += [answer.time_taken.second+float(answer.time_taken.microsecond)/1000000]
	return sum(time)/len(time)
