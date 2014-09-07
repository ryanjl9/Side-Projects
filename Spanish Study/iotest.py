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
						englishList.append(englishWord)
					elif checklen == 's':
						checkWordLength = len(check)
						spanishWord = check[3:checkWordLength]
						bufferlist.remove(check)
						spanishList.append(spanishWord)
listSelecter('test.txt', 18)
print(spanishList)
print(englishList)