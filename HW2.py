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
		self.IOTimeRemaining = IOTime
		self.waitTime = 0

	def __lt__(self,other):
		return self.cpuTime < other.cpuTime

def SJF(processes):
	time = 0
	doneProceeses = 0
	processes.sort()
	while doneProceeses !=cpuBound:

		for i in range(0,numcores):
			if cores[i] == None:
				print str(time) +"ms: added something to core "+ str(i)
				cores[i]  = processes.pop(0)
				continue
			else:
				cores[i].burstTimeRemaining -=1
				if cores[i].burstTimeRemaining ==0:
					print "[time " + str(time) + "ms] Process ID " + str(cores[i].pNum)+" CPU burst done (turnaround time : "+str(time)+ "ms , total wait time "+ str(cores[i].waitTime)+"ms) Core " + str(i)+ " is now free"
					cores[i] = None

					doneProceeses+=1
		for p in processes:
			#print p.waitTime
			p.waitTime+=1

		time+=1
			


def context(processA, processB,time):
	print "[time " + str(time) + "ms] Context switch (swapping out Process ID " + str(processA.pNum) + " for Process ID " + str(processB.pNum) +")"
	
		

def RoundRobin(timeSlice):
		time = 0
		loop = True
		IOQueue = []
		switching = [0,0,0,0]
		while loop:
			for i in range(0, numcores):
				if switching[i] > 0:
					switching[i] -= 1
					continue
				if cores[i] == None:
					cores[i] = readyQueue.pop(0)
					cores[i].timeSlice = 0
				else:
					cores[i].timeSlice += 1
					if cores[i].timeSlice >= timeSlice:
						switching[i] = 2
						print "[time " + str(time) + "ms] Context switch (swapping out process ID " + str(cores[i].pNum) + " for process ID " + str(readyQueue[0].pNum) + ")"
						readyQueue.append(cores[i])
						cores[i] = readyQueue.pop(0)
					cores[i].burstTimeRemaining -= 1
					if cores[i].burstTimeRemaining < 0:
						switching[i] = 2
						if(cores[i].interactive):
							print "[time " + str(time) + "ms] " + "Interactive process ID " + str(cores[i].pNum) + " CPU burst done (turnaround time xms, total wait time xms)"
						else:
							print "[time " + str(time) + "ms] " + "Interactive process ID " + str(cores[i].pNum) + " CPU burst done (turnaround time xms, total wait time xms)"
							cores[i].burstsRemaining -= 1

						print "[time " + str(time) + "ms] Context switch (swapping out process ID " + str(cores[i].pNum) + " for process ID " + str(readyQueue[0].pNum) + ")"
						IOQueue.append(cores[i])
						cores[i] = readyQueue.pop(0)

			for i in range(0, len(IOQueue)):
				IOQueue[i].IOTimeRemaining -= 1
				if IOQueue[i].IOTimeRemaining < 0:
					if(IOQueue[i].interactive):
						IOQueue[i].cpuTime = random.randint(20,200)
					else:
						IOQueue[i].cpuTime = random.randint(200,3000)	
					readyQueue.append(IOQueue.pop(i))
					i-= 1
				loop = False
			time += 1



if __name__ == '__main__':
	n = 12
	numcores = 4
	processes = []
	cores = [None, None, None, None]
	time = 0
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
			print "[time " + str(time) + "ms] CPU Bound process ID " + str(p.pNum) + " entered ready queue (requires " + str(p.cpuTime) + " CPU time; priority " + str(p.priority) + ")"

	#RoundRobin(100)

	readyQueue.sort()

	SJF(readyQueue)
