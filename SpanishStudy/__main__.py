#What runs the program
#This program took 255 lines of code for bare basic functionality easy readability 
import pythonFiles.guiController as guiController 
import pythonFiles.listChecker as listChecker 
import pythonFiles.logicClass as logicClass 
import pythonFiles.startup as startup
import pythonFiles.easygui as easygui
import os, re, sys

""" If you want to run the program from this part file, you will
have to go into listChecker.py and remove the '/Study Spanish' from the file
path on line 5."""

def main():
	startup.main()

if __name__ == '__main__':
	main()