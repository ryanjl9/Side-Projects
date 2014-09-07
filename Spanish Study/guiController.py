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

