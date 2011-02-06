
from game.models import Question

for op in map(str,range(4)):
	for i in range(1,11):
		for j in range (1,11):
			q = Question()
			q.first_number = i
			q.second_number = j
			q.operation = op
			q.save()	
