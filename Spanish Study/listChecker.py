import os, re

listposition = os.chdir('lists')

def inList():
	x = []
	x.append(os.listdir('.'))
	return x[0]
	
def validObject():
	x = []
	cyclelist = inList()
	for element in cyclelist:
		if re.search('.txt', element):
			x.append(element)
	return x

def listLength(list):
	with open(list, "r") as file:
		return len(file.readlines())
	



