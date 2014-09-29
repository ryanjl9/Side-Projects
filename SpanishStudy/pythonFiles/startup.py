#This file was to keep the __main__.py file clean

import guiController, listChecker, logicClass

def main():
	#Initial prompt, returns english or spanish
	x = guiController.startup()
	
	#What list, returns name of list
	y = guiController.selectList()
	
	"""Checks y's length, if the length is none then the program quits, else it goes to 
	the logicClass file to get the words from the list to quiz you on. Unknown why you have 
	to add 1 to z"""
	z = listChecker.listLength(y)
	if z != False:
		c = logicClass.listSelecter(y, z + 1)
	else:
		return False
	
	"""Tells the program whether to quiz in english or spanish and then it goes through and
	asks you the questions."""
	g = logicClass.EorS_return(x)