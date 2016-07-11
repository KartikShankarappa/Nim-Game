import sys
import random

no_of_heaps = random.choice([3,5,7])
heap = []
user = random.choice([0,1])				# if "user" is assigned value 0, then computer goes first, else vice versa
nextMove = ''

def gameInitialSetup():
	for x in range(no_of_heaps):
		no_of_objects = random.choice([9, 11, 13])
		heap.append(no_of_objects)

	print "Created " + str(no_of_heaps) + " heaps of sizes "

	for x in heap:
		print x,
	print ' '


def firstMove():
	if user == 0:
		nextMove = "Computer"
	else:
		nextMove = "Human"

	print "Player " + nextMove + " goes first"
	print "\n"

	return nextMove


def printHeap():
	for x in heap:
		print x,
	print " "


def isLegalMove(input):
	try:
		whichHeap = int(input[1])
		howManyObjects = int(input[0])
	except:
		print "Player Human that is an invalid move. Try Again\n"
		return False 

	if len(input) < 2 or len(input) > 2:
		print "Player Human that is an invalid move. Try Again\n"
		return False
	elif whichHeap <= 0 or whichHeap > len(heap):
		print "Player Human that is an invalid move. You have entered an invalid heap. Try Again\n"
		return False
	elif howManyObjects <= 0 or howManyObjects > heap[whichHeap - 1]:
		print "Player Human that is an invalid move. You have entered an invalid number of objects to be removed. Try Again\n"
		return False
	else:
		return True



def isGameOver():
	numOfObjectsRemaining = 0
	for x in heap:
		numOfObjectsRemaining = numOfObjectsRemaining + x

	if numOfObjectsRemaining == 0:
		return True
	else:
		return False



def human():
	if isGameOver() == True:
		print "Player Computer has won\n"
		sys.exit(0)

	input = raw_input("Player human enter the number of objects (Y) to take from what heap (X)- in order: Y X \n")
	input = input.split()

	while isLegalMove(input) == False:
		input = raw_input("Player human enter the number of objects (Y) to take from what heap (X)- in order: Y X \n")
		input = input.split()

	whichHeap = int(input[1])
	howManyObjects = int(input[0])
	heap[whichHeap - 1] = heap[whichHeap - 1] - howManyObjects
	printHeap()
	nextMove = "Computer"
	computer()



def computer():

	if isGameOver() == True:
		print "Player Human has Won\n"
		sys.exit(0)	

	whichHeap = random.randint(1,len(heap))
	numOfObjectsPresent = heap[whichHeap - 1]

	while numOfObjectsPresent == 0:
		if isGameOver() == True:
			print "Player Human has Won\n"
			sys.exit(0)

		whichHeap = random.randint(1,len(heap))
		numOfObjectsPresent = heap[whichHeap - 1]

	howManyObjects = random.randint (1, heap[whichHeap - 1])
	heap[whichHeap - 1] = heap[whichHeap - 1] - howManyObjects

	print "Player Computer took " + str(howManyObjects) + " from heap " + str(whichHeap) + "\n"

	printHeap()
	nextMove = "Human"
	human()




gameInitialSetup()
firstChance = firstMove()

if firstChance == "Human":
	human()
else:
	computer()





