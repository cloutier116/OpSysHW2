import random
import sys
import copy

#Chris Cloutier
#Parshva Shah

#run with defaults by giving no command line arguments
#Command line arguments are of the form python HW2.py numprocesses, numcores, timeslice

class Process:
	def __init__ (self, pNum, interactive, cpuTime, IOTime, priority, bursts):
		self.state = 0 #0 = ready, 1 = active, 2 = blocked on I/O
		self.pNum = pNum
		self.interactive = interactive
		self.cpuTime = cpuTime
		self.IOTime = IOTime
		self.priority = priority
		self.core = 0
		self.burstsRemaining = bursts
		self.timeSlice = 0
		self.burstTimeRemaining = cpuTime
		self.IOTimeRemaining = IOTime
		self.waitTime = 0
		self.burstTimes = []
		self.waitTimes = []
		self.turnaroundTime = 0
		self.turnaroundTimes = []
		self.totalCPUTime = 0

	def __lt__(self,other):
		return self.cpuTime < other.cpuTime
	def __str__(self):
		if self.interactive:
			return "Interactive Process ID " + str(self.pNum) + " with "+str(self.cpuTime) +" burst time and " + str(self.IOTime)+" IO time needed. "+ str(self.burstTimeRemaining)+ " Burst time remaining. Priority of " + str(self.priority)
		else:
			return "CPU Bound Process ID " + str(self.pNum) + " with "+str(self.cpuTime) +" burst time and " + str(self.IOTime)+" IO time needed "+ str(self.burstTimeRemaining)+ " Burst time remaining. Priority of " + str(self.priority)
		#added helper functions
	def setNewCPU(self,newTime):
		self.cpuTime = newTime
		self.burstTimeRemaining = self.cpuTime
	def setNewIO(self,newTime):
		self.IOTime = newTime
		self.IOTimeRemaining = self.IOTime
	def getTurnaround(self):
		return self.cpuTime+self.waitTime
	def printAvgBurst(self):
		return sum(self.burstTimes)/ float(len(self.burstTimes))
	def printAvgWait(self):
		return sum(self.waitTimes)/ float(len(self.waitTimes))
	def printAvgTurnaround(self):
		return sum(self.turnaroundTimes)/ float(len(self.turnaroundTimes))

def sortByBurst(self,other):
		return self.burstTimeRemaining < other.burstTimeRemaining

def sortByPriority(self,other):
		return self.priority < other.priority

def SJF(myQueue):
	storedQueue = copy.copy(myQueue)
	time = 0
	cpuWait =[0 for i in range(0, numcores)]
	cpuUse = [0 for i in range(0,numcores)]
	IOWait = []
	doneProcesses = 0
	myQueue.sort()
	while doneProcesses !=cpuBound:
		for i in range(0,numcores):
			if cores[i]:
				cpuUse[i] +=1
				cores[i].totalCPUTime += 1
			if cpuWait[i] >0:
				cpuWait[i]-=1
				continue
			if cores[i] == None:
				if myQueue:
					cores[i]  = myQueue.pop(0)
					#print str(time) +"ms: added ID " +str(cores[i].pNum)+ " to core "+ str(i)

					continue
			else:
				cores[i].turnaroundTime += 1
				cores[i].burstTimeRemaining -=1
				if cores[i].burstTimeRemaining ==0:
					if not cores[i].interactive:
						cores[i].burstsRemaining-=1
						if cores[i].burstsRemaining==0:
							print  "[time " + str(time) + "ms] CPU Process ID " + str(cores[i].pNum) +" terminated " 
							doneProcesses+=1
						else:
							print "[time " + str(time) + "ms] CPU Process ID " + str(cores[i].pNum)+" CPU burst done (turnaround time : "+str(cores[i].cpuTime+ cores[i].waitTime )+ "ms , total wait time "+ str(cores[i].waitTime)+"ms)"
							if myQueue:
								context(cores[i],myQueue[0],time)
							else:
								print "[time " + str(time) + "ms] Context switch (swapping out Process ID " + str(cores[i].pNum) + " for None)"

					else:
						
						print "[time " + str(time) + "ms] Interactive Process ID " + str(cores[i].pNum)+" CPU burst done (turnaround time : "+str(cores[i].cpuTime+ cores[i].waitTime )+ "ms , total wait time "+ str(cores[i].waitTime)+"ms)"
						if myQueue:
								context(cores[i],myQueue[0],time)
						else:
							print "[time " + str(time) + "ms] Context switch (swapping out Process ID " + str(cores[i].pNum) + " for None)"


					

					IOWait.append( cores[i])
					if myQueue:
						cores[i] = myQueue.pop(0)
					else:
						cores[i] = None


					
					cpuWait[i] = 2
		for p in myQueue:
			#print p.waitTime
			p.waitTime+=1
			p.turnaroundTime += 1


		if(len(IOWait) != 0):
			returnQueue = []
			returnQueue[:] = [x for x in IOWait if x.IOTimeRemaining <= 1]
			IOWait[:] = [x for x in IOWait if x.IOTimeRemaining > 1]
			for i in IOWait:
				i.IOTimeRemaining -= 1
			for i in returnQueue:
				#print "Core " + str(IOQueue[i].pNum) + " time remaining is " + str(IOQueue[i].IOTimeRemaining)
				if i.interactive:
					i.setNewCPU(random.randint(20,200))
					i.setNewIO(random.randint(1000,4500))
					i.waitTimes.append(i.waitTime)
					i.waitTime = 0
					i.turnaroundTimes.append(i.turnaroundTime)
					i.turnaroundTime = 0
					print "[time " + str(time) + "ms] Interactive process ID " + str(i.pNum) + " entered ready queue (requires " + str(i.cpuTime) +  "ms CPU time; priority " + str(i.priority) + ")"
				else:
					#i.waitTime = 0
					i.setNewCPU(random.randint(200,3000))
					i.setNewIO(random.randint(1200,3200))   
					i.waitTimes.append(i.waitTime)
					i.waitTime = 0      
					i.turnaroundTimes.append(i.turnaroundTime)
					i.turnaroundTime = 0                
					print "[time " + str(time) + "ms] CPU Bound process ID " + str(i.pNum) + " entered ready queue (requires " + str(i.cpuTime) + "ms CPU time; priority " + str(i.priority) + ")"
				if i.burstsRemaining > 0:
					myQueue.append(i)
		

		time+=1

		myQueue.sort()
	
	if cpuBound > 0:
		minTurn = storedQueue[0].turnaroundTimes[0]
		maxTurn = storedQueue[0].turnaroundTimes[0]
		avgTurn = 0
		minWait = storedQueue[0].waitTimes[0]
		maxWait = storedQueue[0].waitTimes[0]
		avgWait = 0
		for process in storedQueue:
			for processtime in process.turnaroundTimes:
				if processtime < minTurn:
					minTurn = processtime
				if processtime > maxTurn:
					maxTurn = processtime
				avgTurn += processtime
			for processtime in process.waitTimes:
				if processtime < minWait:
					minWait = processtime
				if processtime > maxWait:
					maxWait = processtime
				avgWait += processtime
		avgTurn /= float(bursts*len(storedQueue))
		avgWait /= float(bursts*len(storedQueue))
		print ("Turnaround time: min %.3f ms; avg %.3f ms; max %.3f ms" % (minTurn, avgTurn, maxTurn))
		print ("Total wait time: min %.3f ms; avg %.3f ms; max %.3f ms" % (minWait, avgWait, maxWait))
		print "Average CPU utilization: %.3f%%" % (sum(cpuUse)/float(time * numcores) * 100)
		print "Average CPU utilization per process:"
		for process in storedQueue:
			print "process ID %d: %.3f%%" %(process.pNum , process.totalCPUTime/float(time * numcores) * 100)
							


def SJFPreempt(inputQueue):
	myQueue = inputQueue[:]
	storedQueue = copy.copy(myQueue)
	time = 0
	cpuWait = [0 for x in range(0,numcores)]
	cpuUse = [0 for i in range(0,numcores)]
	IOWait = []
	doneProcesses = 0
	#myQueue.sort()
	myQueue = sorted(myQueue, key=lambda process: process.burstTimeRemaining)
	while doneProcesses !=cpuBound:
		for i in range(0,numcores):
			if cpuWait[i] >0:
				cpuWait[i]-=1
				continue
			if cores[i]:
				cpuUse[i] += 1
				cores[i].totalCPUTime += 1
			if cores[i] == None:
				if myQueue:
					cores[i]  = myQueue.pop(0)
					#print str(time) +"ms: added ID " +str(cores[i].pNum)+ " to core "+ str(i)

					continue
			else:
				cores[i].turnaroundTime += 1
				cores[i].burstTimeRemaining -=1
				if cores[i].burstTimeRemaining ==0:
					if not cores[i].interactive:
						cores[i].burstsRemaining-=1
						if cores[i].burstsRemaining==0:
							print  "[time " + str(time) + "ms] CPU Process ID " + str(cores[i].pNum) +" terminated " 
							doneProcesses+=1
						else:
							print "[time " + str(time) + "ms] CPU Process ID " + str(cores[i].pNum)+" CPU burst done (turnaround time : "+str(cores[i].cpuTime+ cores[i].waitTime )+ "ms , total wait time "+ str(cores[i].waitTime)+"ms)"
							if myQueue:
								context(cores[i],myQueue[0],time)
							else:
								print "[time " + str(time) + "ms] Context switch (swapping out Process ID " + str(cores[i].pNum) + " for None)"

					else:
						
						print "[time " + str(time) + "ms] Interactive Process ID " + str(cores[i].pNum)+" CPU burst done (turnaround time : "+str(cores[i].cpuTime+ cores[i].waitTime )+ "ms , total wait time "+ str(cores[i].waitTime)+"ms)"
						if myQueue:
								context(cores[i],myQueue[0],time)
						else:
							print "[time " + str(time) + "ms] Context switch (swapping out Process ID " + str(cores[i].pNum) + " for None)"


					

					IOWait.append( cores[i])
					if myQueue:
						cores[i] = myQueue.pop(0)
					else:
						cores[i] = None


					
					cpuWait[i] = 2
		for p in myQueue:
			#print p.waitTime
			p.waitTime+=1
			p.turnaroundTime += 1


		if(len(IOWait) != 0):
			returnQueue = []
			returnQueue[:] = [x for x in IOWait if x.IOTimeRemaining <= 1]
			IOWait[:] = [x for x in IOWait if x.IOTimeRemaining > 1]
			for i in IOWait:
				i.IOTimeRemaining -= 1
			for i in returnQueue:
				#print "Core " + str(IOQueue[i].pNum) + " time remaining is " + str(IOQueue[i].IOTimeRemaining)
				if i.interactive:
					i.setNewCPU(random.randint(20,200))
					i.setNewIO(random.randint(1000,4500))
					i.waitTimes.append(i.waitTime)
					i.waitTime = 0
					i.turnaroundTimes.append(i.turnaroundTime)
					i.turnaroundTime = 0
					print "[time " + str(time) + "ms] Interactive process ID " + str(i.pNum) + " entered ready queue (requires " + str(i.cpuTime) +  "ms CPU time; priority " + str(i.priority) + ")"
					longestCore = None
					for j in range(0, numcores):
						if cores[j]:
							if longestCore:
								if cores[j].burstTimeRemaining > cores[longestCore].burstTimeRemaining:
									longestCore = j
							else:
								longestCore = j
				 
					if longestCore and i.burstTimeRemaining < cores[longestCore].burstTimeRemaining:
						
						context(cores[longestCore], i, time)
						
 						if cores[longestCore] not in myQueue:
							myQueue.append(cores[longestCore])
						
						
						
						cores[longestCore] = i
						cpuWait[longestCore] = 2
					else:

						myQueue.append(i)	
				else:
					#i.waitTime = 0
					i.setNewCPU(random.randint(200,3000))
					i.setNewIO(random.randint(1200,3200))   
					i.waitTimes.append(i.waitTime)
					i.waitTime = 0      
					i.turnaroundTimes.append(i.turnaroundTime)
					i.turnaroundTime = 0    
					print "[time " + str(time) + "ms] CPU Bound process ID " + str(i.pNum) + " entered ready queue (requires " + str(i.cpuTime) + "ms CPU time; priority " + str(i.priority) + ")"
					longestCore = None
					for j in range(0, numcores):
						if cores[j]:
							if longestCore:
								if cores[j].burstTimeRemaining > cores[longestCore].burstTimeRemaining:
									longestCore = j
							else:
								longestCore = j
				 
					if longestCore and i.burstTimeRemaining < cores[longestCore].burstTimeRemaining:
						
						context(cores[longestCore], i, time)
						
						myQueue.append(cores[longestCore])
						
						cores[longestCore] = i
						cpuWait[longestCore] = 2
					else:
						myQueue.append(i)

		
		time+=1

		#myQueue.sort(sortByBurst)
		myQueue = sorted(myQueue, key=lambda process: process.burstTimeRemaining)
	if cpuBound > 0:
		minTurn = storedQueue[0].turnaroundTimes[0]
		maxTurn = storedQueue[0].turnaroundTimes[0]
		avgTurn = 0
		minWait = storedQueue[0].waitTimes[0]
		maxWait = storedQueue[0].waitTimes[0]
		avgWait = 0
		if storedQueue:
			for process in storedQueue:
				for processtime in process.turnaroundTimes:
					if processtime < minTurn:
						minTurn = processtime
					if processtime > maxTurn:
						maxTurn = processtime
					avgTurn += processtime
				for processtime in process.waitTimes:
					if processtime < minWait:
						minWait = processtime
					if processtime > maxWait:
						maxWait = processtime
					avgWait += processtime
			avgTurn /= float(bursts*len(storedQueue))
			avgWait /= float(bursts*len(storedQueue))
			print ("Turnaround time: min %.3f ms; avg %.3f ms; max %.3f ms" % (minTurn, avgTurn, maxTurn))
			print ("Total wait time: min %.3f ms; avg %.3f ms; max %.3f ms" % (minWait, avgWait, maxWait))
			print "Average CPU utilization: %.3f%%" % (sum(cpuUse)/float(time * numcores) * 100)
			print "Average CPU utilization per process:"
			for process in storedQueue:
				print "process ID %d: %.3f%%" %(process.pNum , process.totalCPUTime/float(time * numcores) * 100)
				


def context(processA, processB,time):
	if not processB:
		print "[time " + str(time) + "ms] Context switch (swapping out Process ID " + str(processA.pNum) + " for None)"
	else:
		print "[time " + str(time) + "ms] Context switch (swapping out Process ID " + str(processA.pNum) + " for Process ID " + str(processB.pNum) +")"
	
def PriorityAlgo(inputQueue):
	myQueue = inputQueue[:]
	storedQueue = copy.copy(myQueue)
	time = 0
	cpuWait = [0 for x in range(0,numcores)]
	cpuUse = [0 for i in range(0,numcores)]
	IOWait = []
	doneProcesses = 0
	#myQueue.sort()
	myQueue = sorted(myQueue, key=lambda process: process.priority)
	while doneProcesses !=cpuBound:
		for i in range(0,numcores):
			if cpuWait[i] >0:
				cpuWait[i]-=1
				continue
			if cores[i]:
				cpuUse[i] += 1
				cores[i].totalCPUTime += 1
			if cores[i] == None:
				if myQueue:
					cores[i]  = myQueue.pop(0)
					#print str(time) +"ms: added ID " +str(cores[i].pNum)+ " to core "+ str(i)

					continue
			else:
				cores[i].turnaroundTime += 1
				cores[i].burstTimeRemaining -=1
				if cores[i].burstTimeRemaining ==0:
					if not cores[i].interactive:
						cores[i].burstsRemaining-=1
						if cores[i].burstsRemaining==0:
							print  "[time " + str(time) + "ms] CPU Process ID " + str(cores[i].pNum) +" terminated " 
							doneProcesses+=1
						else:
							print "[time " + str(time) + "ms] CPU Process ID " + str(cores[i].pNum)+" CPU burst done (turnaround time : "+str(cores[i].cpuTime+ cores[i].waitTime )+ "ms , total wait time "+ str(cores[i].waitTime)+"ms)"
							if myQueue:
								context(cores[i],myQueue[0],time)
							else:
								print "[time " + str(time) + "ms] Context switch (swapping out Process ID " + str(cores[i].pNum) + " for None)"

					else:
						
						print "[time " + str(time) + "ms] Interactive Process ID " + str(cores[i].pNum)+" CPU burst done (turnaround time : "+str(cores[i].cpuTime+ cores[i].waitTime )+ "ms , total wait time "+ str(cores[i].waitTime)+"ms)"
						if myQueue:
								context(cores[i],myQueue[0],time)
						else:
							print "[time " + str(time) + "ms] Context switch (swapping out Process ID " + str(cores[i].pNum) + " for None)"


					

					IOWait.append( cores[i])
					if myQueue:
						cores[i] = myQueue.pop(0)
					else:
						cores[i] = None


					cpuWait[i] = 2
		for p in myQueue:
			#print p.waitTime
			p.waitTime+=1
			if p.waitTime  %  1200 == 0 and p.priority > 0:
				p.priority -=1
				if p.interactive:
					print "[time " + str(time) + "ms] Increased priority of IO-bound process ID " + str(p.pNum)+ " to "+ str(p.priority)+ "  due to aging"
				else:
					print "[time " + str(time) + "ms] Increased priority of CPU-bound process ID " + str(p.pNum)+ " to "+ str(p.priority)+ "  due to aging"

				
			p.turnaroundTime += 1


		if(len(IOWait) != 0):
			returnQueue = []
			returnQueue[:] = [x for x in IOWait if x.IOTimeRemaining <= 1]
			IOWait[:] = [x for x in IOWait if x.IOTimeRemaining > 1]
			for i in IOWait:
				i.IOTimeRemaining -= 1
			for i in returnQueue:
				#print "Core " + str(IOQueue[i].pNum) + " time remaining is " + str(IOQueue[i].IOTimeRemaining)
				if i.interactive:
					i.setNewCPU(random.randint(20,200))
					i.setNewIO(random.randint(1000,4500))
					i.waitTimes.append(i.waitTime)
					i.waitTime = 0
					i.turnaroundTimes.append(i.turnaroundTime)
					i.turnaroundTime = 0
					print "[time " + str(time) + "ms] Interactive process ID " + str(i.pNum) + " entered ready queue (requires " + str(i.cpuTime) +  "ms CPU time; priority " + str(i.priority) + ")"
					importantCore = None
					for j in range(0, numcores):
						if cores[j]:
							if importantCore:
								if cores[j].priority > cores[importantCore].priority:
									importantCore = j
							else:
								importantCore = j
				 
					if importantCore and i.priority < cores[importantCore].priority:
						
						context(cores[importantCore], i, time)
						
 						if cores[importantCore] not in myQueue:
							myQueue.append(cores[importantCore])
						
						
						
						cores[importantCore] = i
						cpuWait[importantCore] = 2
					else:

						myQueue.append(i)	
				else:
					#i.waitTime = 0
					i.setNewCPU(random.randint(200,3000))
					i.setNewIO(random.randint(1200,3200))   
					i.waitTimes.append(i.waitTime)
					i.waitTime = 0      
					i.turnaroundTimes.append(i.turnaroundTime)
					i.turnaroundTime = 0    
					print "[time " + str(time) + "ms] CPU Bound process ID " + str(i.pNum) + " entered ready queue (requires " + str(i.cpuTime) + "ms CPU time; priority " + str(i.priority) + ")"
					importantCore = None
					for j in range(0, numcores):
						if cores[j]:
							if importantCore:
								if cores[j].priority < cores[importantCore].priority:
									importantCore = j
							else:
								importantCore = j
				 
					if importantCore and i.priority > cores[importantCore].priority:
						
						context(cores[importantCore], i, time)
						
						myQueue.append(cores[importantCore])
						
						cores[importantCore] = i
						cpuWait[importantCore] = 2
					else:
						myQueue.append(i)

		
		time+=1

		#myQueue.sort(sortByBurst)
		myQueue = sorted(myQueue, key=lambda process: process.priority)
	if cpuBound > 0:
		minTurn = storedQueue[0].turnaroundTimes[0]
		maxTurn = storedQueue[0].turnaroundTimes[0]
		avgTurn = 0
		minWait = storedQueue[0].waitTimes[0]
		maxWait = storedQueue[0].waitTimes[0]
		avgWait = 0
		if storedQueue:
			for process in storedQueue:
				for processtime in process.turnaroundTimes:
					if processtime < minTurn:
						minTurn = processtime
					if processtime > maxTurn:
						maxTurn = processtime
					avgTurn += processtime
				for processtime in process.waitTimes:
					if processtime < minWait:
						minWait = processtime
					if processtime > maxWait:
						maxWait = processtime
					avgWait += processtime
			avgTurn /= float(bursts*len(storedQueue))
			avgWait /= float(bursts*len(storedQueue))
			print ("Turnaround time: min %.3f ms; avg %.3f ms; max %.3f ms" % (minTurn, avgTurn, maxTurn))
			print ("Total wait time: min %.3f ms; avg %.3f ms; max %.3f ms" % (minWait, avgWait, maxWait))
			print "Average CPU utilization: %.3f%%" % (sum(cpuUse)/float(time * numcores) * 100)
			print "Average CPU utilization per process:"
			for process in storedQueue:
				print "process ID %d: %.3f%%" %(process.pNum , process.totalCPUTime/float(time * numcores) * 100)
				
		

def RoundRobin(timeSlice, readyQueue):
		storedQueue = copy.copy(readyQueue)
		time = 0
		myQueue = readyQueue[:]
		IOQueue = []
		switching = [0 for i in range(0, numcores)]
		cpuUse = [0 for i in range(0,numcores)]
		finished = 0

		while finished != cpuBound:
			time += 1
			for i in range(0, numcores):
				if switching[i] > 0:
					switching[i] -= 1
					continue
				if cores[i]:
					cpuUse[i] += 1
					cores[i].totalCPUTime += 1
				if cores[i] == None:
					if len(myQueue) > 0:
						cores[i] = myQueue.pop(0)
						cores[i].timeSlice = 0
						switching[i] = 2
						print "[time " + str(time) + "ms] Context switch (swapping out nothing for process ID " + str(cores[i].pNum) + ")"

				else:
					#print "Process " + str(cores[i].pNum) + " Timeslice = " +  str(cores[i].timeSlice)
					cores[i].timeSlice += 1
					cores[i].turnaroundTime += 1
					if cores[i].timeSlice >= timeSlice:
						switching[i] = 2
						if len(myQueue) > 0:
							print "[time " + str(time) + "ms] Context switch (swapping out process ID " + str(cores[i].pNum) + " for process ID " + str(myQueue[0].pNum) + ")"
							myQueue.append(cores[i])
							cores[i].turnaroundTime += 2
							cores[i] = myQueue.pop(0)
							cores[i].timeSlice = 0
						

					cores[i].burstTimeRemaining -= 1
					if cores[i].burstTimeRemaining < 0:
						switching[i] = 2
						if(cores[i].interactive):
							print "[time " + str(time) + "ms] " + "Interactive process ID " + str(cores[i].pNum) + " CPU burst done (turnaround time " + str(cores[i].turnaroundTime) + "ms, total wait time " + str(cores[i].waitTime) + "ms)"
						else:
							cores[i].burstsRemaining -= 1
							if cores[i].burstsRemaining <= 0:
								print ("[time " + str(time) + "ms] " + "CPU-bound process ID " + str(cores[i].pNum) + " terminated (avg turnaround time %.3fms, avg total wait time %.3fms)" % (cores[i].printAvgTurnaround(), cores[i].printAvgWait()))
								finished += 1
							else:
								print "[time " + str(time) + "ms] " + "CPU-bound process ID " + str(cores[i].pNum) + " CPU burst done (turnaround time " + str(cores[i].turnaroundTime) + "ms, total wait time " + str(cores[i].waitTime) + "ms)"
						if len(myQueue) > 0:
							print "[time " + str(time) + "ms] Context switch (swapping out process ID " + str(cores[i].pNum) + " for process ID " + str(myQueue[0].pNum) + ")"
							IOQueue.append(cores[i])
							cores[i] = myQueue.pop(0)
							cores[i].timeSlice = 0
						else:
							print "[time " + str(time) + "ms] Context switch (swapping out process ID " + str(cores[i].pNum) + " for nothing)"
							IOQueue.append(cores[i])
							cores[i] = None
							continue
			
			if(len(IOQueue) != 0):
				returnQueue = []
				returnQueue[:] = [x for x in IOQueue if x.IOTimeRemaining <= 1]
				IOQueue[:] = [x for x in IOQueue if x.IOTimeRemaining > 1]
				for i in IOQueue:
					i.IOTimeRemaining -= 1
				for i in returnQueue:
					#print "Core " + str(IOQueue[i].pNum) + " time remaining is " + str(IOQueue[i].IOTimeRemaining)
					if i.interactive:
						i.setNewCPU(random.randint(20,200))
						i.setNewIO(random.randint(1000,4500))
						i.waitTimes.append(i.waitTime)
						i.waitTime = 0
						i.turnaroundTimes.append(i.turnaroundTime)
						i.turnaroundTime = 0
						print "[time " + str(time) + "ms] Interactive process ID " + str(i.pNum) + " entered ready queue (requires " + str(i.cpuTime) +  "ms CPU time; priority " + str(i.priority) + ")"
					else:
						#i.waitTime = 0
						i.setNewCPU(random.randint(200,3000))
						i.setNewIO(random.randint(1200,3200))   
						i.waitTimes.append(i.waitTime)
						i.waitTime = 0      
						i.turnaroundTimes.append(i.turnaroundTime)
						i.turnaroundTime = 0                
						print "[time " + str(time) + "ms] CPU-bound process ID " + str(i.pNum) + " entered ready queue (requires " + str(i.cpuTime) + "ms CPU time; priority " + str(i.priority) + ")"
					if i.burstsRemaining > 0:
						myQueue.append(i)
				

			for p in myQueue:
				p.waitTime+=1
				p.turnaroundTime += 1

		if cpuBound > 0:
			minTurn = storedQueue[0].turnaroundTimes[0]
			maxTurn = storedQueue[0].turnaroundTimes[0]
			avgTurn = 0
			minWait = storedQueue[0].waitTimes[0]
			maxWait = storedQueue[0].waitTimes[0]
			avgWait = 0
			for process in storedQueue:
				for processtime in process.turnaroundTimes:
					if time < minTurn:
						minTurn = processtime
					if processtime > maxTurn:
						maxTurn = processtime
					avgTurn += processtime
				for processtime in process.waitTimes:
					if processtime < minWait:
						minWait = processtime
					if processtime > maxWait:
						maxWait = processtime
					avgWait += processtime
			avgTurn /= float(bursts*len(storedQueue))
			avgWait /= float(bursts*len(storedQueue))
			print ("Turnaround time: min %.3f ms; avg %.3f ms; max %.3f ms" % (minTurn, avgTurn, maxTurn))
			print ("Total wait time: min %.3f ms; avg %.3f ms; max %.3f ms" % (minWait, avgWait, maxWait))
			print "Average CPU utilization: %.3f%%" % (sum(cpuUse)/float(time * numcores) * 100)
			print "Average CPU utilization per process:"
			for process in storedQueue:
				print "process ID %d: %.3f%%" %(process.pNum , process.totalCPUTime/float(time * numcores) * 100)

if __name__ == '__main__':
	#arguments are number of processes, number of cores, timeslice for RR
	n = 12
	numcores = 4
	processes = []
	
	time = 0
	cpuBound = 0
	bursts = 8
	timeslice = 100

	if len(sys.argv) != 1:
		if len(sys.argv) >= 2 and sys.argv[1] and int(sys.argv[1]) >= 1:
			n = int(sys.argv[1])
		if len(sys.argv) >= 3 and sys.argv[2] and int(sys.argv[2]) >= 1:
			numcores = int(sys.argv[2])
		if len(sys.argv) >= 4 and sys.argv[3] and int(sys.argv[3]) >= 1:
			timeslice = int(sys.argv[3])


	cores = [None for i in range(0,numcores) ]
	for i in range(1,n+1):
		if i > n/3:
			processes.append(Process(i, True, random.randint(20,200), random.randint(1000,4500), random.randint(0,4),bursts))
		else:
			cpuBound +=1
			processes.append(Process(i, False, random.randint(200,3000), random.randint(1200, 3200), random.randint(0,4),bursts))

	random.shuffle(processes)

	for i in range(0,len(processes)):
		processes[i].pNum = i+1
	
	readyQueue = []
	for p in processes:
		readyQueue.append(p)
		if(p.interactive):
			print "[time " + str(time) + "ms] Interactive process ID " + str(p.pNum) + " entered ready queue (requires " + str(p.cpuTime) +  "ms CPU time; priority " + str(p.priority) + ")"
		else:
			print "[time " + str(time) + "ms] CPU-bound process ID " + str(p.pNum) + " entered ready queue (requires " + str(p.cpuTime) + "ms CPU time; priority " + str(p.priority) + ")"


	print "=============== DOING SJF ==============="
	SJF(copy.deepcopy(readyQueue))

	print
	time = 0
	for p in processes:
		if(p.interactive):
			print "[time " + str(time) + "ms] Interactive process ID " + str(p.pNum) + " entered ready queue (requires " + str(p.cpuTime) +  "ms CPU time; priority " + str(p.priority) + ")"
		else:
			print "[time " + str(time) + "ms] CPU-ound process ID " + str(p.pNum) + " entered ready queue (requires " + str(p.cpuTime) + "ms CPU time; priority " + str(p.priority) + ")"
	
	print "=====================DOING SRT======================"
	cores = [None for i in range(0,numcores) ]

	SJFPreempt(copy.deepcopy(readyQueue))

	print
	time = 0
	for p in processes:
		if(p.interactive):
			print "[time " + str(time) + "ms] Interactive process ID " + str(p.pNum) + " entered ready queue (requires " + str(p.cpuTime) +  "ms CPU time; priority " + str(p.priority) + ")"
		else:
			print "[time " + str(time) + "ms] CPU-bound process ID " + str(p.pNum) + " entered ready queue (requires " + str(p.cpuTime) + "ms CPU time; priority " + str(p.priority) + ")"

	print "=================DOING RR==============="
	cores = [None for i in range(0,numcores) ]

	RoundRobin(timeslice, copy.deepcopy(readyQueue)) 
	print

	time = 0
	for p in processes:
		if(p.interactive):
			print "[time " + str(time) + "ms] Interactive process ID " + str(p.pNum) + " entered ready queue (requires " + str(p.cpuTime) +  "ms CPU time; priority " + str(p.priority) + ")"
		else:
			print "[time " + str(time) + "ms] CPU-bound process ID " + str(p.pNum) + " entered ready queue (requires " + str(p.cpuTime) + "ms CPU time; priority " + str(p.priority) + ")"

		
	print"===================DOING PRIORITY====================== "
	cores = [None for i in range(0,numcores) ]

	PriorityAlgo(copy.deepcopy(readyQueue)) 
