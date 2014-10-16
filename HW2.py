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
		self.timeSlice = 0
		self.burstTimeRemaining = cpuTime

	def __lt__(self,other):
		return self.cpuTime < other.cpuTime

def RoundRobin(timeSlice):
		time = 0
		loop = True
		while loop:
			for i in range(0,numCPUs):
				if CPUs[i] == None:
					CPUs[i] = readyQueue.pop(0)
					CPUs[i].timeSlice = 0
				else:
					CPUs[i].timeSlice += 1
					if CPUs[i].timeSlice >= timeSlice:
						print "[time " + str(time) + "ms] Context switch (swapping out process ID " + str(CPUs[i].pNum) + " for process ID " + str(readyQueue[0].pNum) + ")"
						readyQueue.append(CPUs[i])
						CPUs[i] = readyQueue.pop(0)
						loop = False
			time += 1



			#break
		for CPU in CPUs:
			print CPU.pNum

if __name__ == '__main__':
	n = 12
	numCPUs = 4
	processes = []
	CPUs = [None, None, None, None]
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
			print "[time " + str(time) + "ms] Interactive process ID " + str(p.pNum) + " entered ready queue (requires " + str(p.cpuTime) +  " CPU time; priority " + str(p.priority) + ")"
		else:
			print "[time " + str(time) + "ms] CPU Bound process ID " + str(p.pNum) + " entered ready queue (requires " + str(p.cpuTime) + " CPU time; priority " + str(p.priority) + ")"
	readyQueue.sort()

	RoundRobin(100)


	
