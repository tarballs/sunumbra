# gui elements
global header
global mainmenu
global gameheader
global line
global dashline

import os

# loads gui elements from txt files
header = ''
with open('graphics/header.txt','r') as fp:
	for x in fp:
		header = header + x
mainmenu = ''
with open('graphics/mainmenu.txt','r') as fp:
	for x in fp:
		mainmenu = mainmenu + x
gameheader = ''
with open('graphics/gameheader.txt','r') as fp:
	for x in fp:
		gameheader = gameheader + x
line = ' '
for x in range(0,119):
	line = line + '_'
dashline = ' '
for x in range(0,119):
	line = line + '-'

def getinput():
	keyin = input("  Selection: ")
	return keyin

def clear():
	os.system('cls')
	print(header)

def menu():
	clear()
	print(mainmenu)

def display(description, node):
	clear()
	print(gameheader)
	for i in description:
		print(' ',i)
	print(dashline)
	for i, item in enumerate(node):
		print(' ',i+1,":",item)
	print()
