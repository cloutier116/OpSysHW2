import random

class Process:
	def __init__ (self, pNum, interactive, cpuTime, IOTime, priority):
		self.state = 0 #0 = ready, 1 = active, 2 = blocked on I/O
		self.pNum = pNum
		self.interactive = interactive
		self.cpuTime = cpuTime
		self.IOTime = IOTime
		self.priority = priority
		self.core = 0
		self.burstsRemaining = 8

n = 12
numCPUs = 4
processes = []
time = 0

for i in range(1,n+1):
	if(random.randint(0,100) < 80):
		processes.append(Process(i, True, random.randint(20,200), random.randint(1000,4500), random.randint(0,4)))
	else:
		processes.append(Process(i, False, random.randint(200,3000), random.randint(1200, 3200), random.randint(0,4)))

readyQueue = []
for p in processes:
	readyQueue.append(p)
	if(p.interactive):
		print "Interactive process ID " + str(p.pNum) + " entered ready queue (requires " + str(p.cpuTime) +  " CPU time; priority " + str(p.priority) + ")"
	else:
		print "CPU Bound process ID " + str(p.pNum) + " entered ready queue (requires " + str(p.cpuTime) + " CPU time; priority " + str(p.priority) + ")"

