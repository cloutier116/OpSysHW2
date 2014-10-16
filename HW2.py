import random

class Process:
	def __init__ (self, _pPum, _interative):
		state = "ready"
		pNum = pNum
		interactive = _interactive

n = 12
processes = []

for i in range(1,n+1):
	if(random.range(0,100) < 80):
		processes[i] = Process(i, True)
	else:
		processes[i] = Process(i, False)
