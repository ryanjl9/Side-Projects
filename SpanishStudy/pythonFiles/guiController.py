#What controls all of the GUI's 

import easygui, listChecker

#Easy default title
title = 'Spanish Study'

#Prompts the user for spanish or english quizzing
def startup():
	x = easygui.buttonbox(msg = 'Please select whether you want to be' +
	' quized in either Spanish or English', title = title, choices=('Spanish', 'English'))
	if x =='Spanish':
		return 'spanish'
	elif x == 'English':
		return 'english'

#List of all possible lists the be quizzed from
def selectList():
	y = listChecker.validObject()
	x = easygui.choicebox(msg = 'Please select a list of words'\
	, title = title, choices = y)
	return x
	
#The box that the user uses to type their answer
def userQuestion(languageValue):
	x = easygui.enterbox(msg = "Enter the word for " + languageValue, title = title)
	return x

#Tells the user what answers were wrong
def wrongAnswer(x):
    c = 2
    eng = ''
    spanish = ''
    leng = len(x)
    for y in x:
        if c % 2 == 0:
            eng = x[c-2]
            c += 1
        else:
           spanish = x[c-2]
           c += 1
           texbox = easygui.msgbox('You put %s instead of %s' % (eng, spanish))
           eng = ''
           spanish = ''