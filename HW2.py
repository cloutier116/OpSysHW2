import random
import sys
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

	def __lt__(self,other):
			return self.cpuTime < other.cpuTime

def SJF(processes):
	time = 0
	doneProceeses = 0
	processes.sort()
	while doneProceeses !=cpuBound:
		time+=1
		for p in processes:
			for core in cores:
				if core!=None
					core = p

		doneProceeses +=1


def context(processA, processB,time):
	print "[time " + str(time) + "ms] Context switch (swapping out Process " + str(processA.pNum) + " for Process " + str(processB.pNum) 
		


if __name__ == '__main__':
	n = 12
	numCPUs = 4
	processes = []
	time = 0
	cores = [None,None,None,None]
	cpuBound = 0



	for i in range(1,n+1):
		if(random.randint(0,100) < 80):
			processes.append(Process(i, True, random.randint(20,200), random.randint(1000,4500), random.randint(0,4)))
		else:
			cpuBound +=1
			processes.append(Process(i, False, random.randint(200,3000), random.randint(1200, 3200), random.randint(0,4)))

	readyQueue = []
	for p in processes:
		readyQueue.append(p)
		if(p.interactive):
			print "[time " + str(time) + "ms] Interactive process ID " + str(p.pNum) + " entered ready queue (requires " + str(p.cpuTime) +  "ms CPU time; priority " + str(p.priority) + ")"
		else:
			print "[time " + str(time) + "ms] CPU Bound process ID " + str(p.pNum) + " entered ready queue (requires " + str(p.cpuTime) + "ms CPU time; priority " + str(p.priority) + ")"

	SJF(readyQueue)
