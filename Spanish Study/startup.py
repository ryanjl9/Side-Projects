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
        for