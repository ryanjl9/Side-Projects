import guiController, os, startup, random, easygui, listChecker

def errorHandler(arg):
	if arg == 'error':
		startup.main()

englishList = []
spanishList = []

def listSelecter(list, length):
	with open(list, "r") as file:
		bufferlist = []
		englishWord = ''
		spanishWord = ''
		for x in range(0,length):
			line = file.readline()
			bufferlist.append(line)
			if len(bufferlist) == 2:
				for check in bufferlist:
					checklen = check[0:1]
					if checklen == 'e':
						checkWordLength = len(check)
						englishWord = check[3:checkWordLength]
						bufferlist.remove(check)	
						englishList.append(englishWord.rstrip("\n"))
					elif checklen == 's':
						checkWordLength = len(check)
						spanishWord = check[3:checkWordLength]
						bufferlist.remove(check)
						spanishList.append(spanishWord.rstrip("\n"))

def randomList():
 	numList = []
	while len(numList) != len(spanishList):
		y = random.randint(0, len(spanishList)-1)
		if y not in numList:
			numList.append(y)
	return numList

def EorS_return(inputs):
	i = 0
	b = 0
	numList = randomList()
	lenofList = len(numList)
	if inputs == 'e':
		while lenofList:
			for x in numList:
				lenofList -= 1
				userAnswer = guiController.userQuestion(englishList[x-2])
				if userAnswer == spanishList[x-2]:	
					i += 1
				else:
					b += 1
		else:
			easygui.msgbox(msg = "You got %s wrong and %s right" % (b,i))
	elif inputs == 's':
		while lenofList:
			for x in numList:
				lenofList -= 1
				userAnswer = guiController.userQuestion(spanishList[x-2])
				if userAnswer == englishList[x-2]:	
					i += 1
				else:
					b += 1
		else:
			easygui.msgbox(msg = "You got %s wrong and %s right" % (b,i))
			








