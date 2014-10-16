import random

class Process:
	def __init__ (self, _pNum, _interactive):
		self.state = 0 #0 = ready, 1 = active, 2 = blocked on I/O
		self.pNum = _pNum
		self.interactive = _interactive

n = 12
processes = []

for i in range(1,n+1):
	if(random.randint(0,100) < 80):
		processes.append(Process(i, True))
	else:
		processes.append(Process(i, False))

print processes
