import easygui
import listChecker

title = 'Spanish Study'

def startup():
	x = easygui.enterbox(msg = 'Please type (s) if you want to be quizzed in Spanish\
 or type (e) if you want to be quizzed in English', title = title)
	if x =='s':
		return 's'
	elif x == 'e':
		return 'e'
	else:
		return 'error'

def selectList():
	y = listChecker.validObject()
	x = easygui.choicebox(msg = 'Please select a list of words'\
	, title = title, choices = y)
	return x
	
def userQuestion(languageValue):
	x = easygui.enterbox(msg = "Enter the word for " + languageValue, title = title)
	return x

def wrongAnswers(x, y):	
	#Color Text
	x = easygui.msgbox(msg = "You put " + x + "when it should have been " + y)

