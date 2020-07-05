# gui.py
"""
should control all user input and visuall information
"""
import os


# startup !add new gui elements here!
def load_element():
	"""
	prewritten 'screens', headers etc are stored in sep txt files for easier reading/editing. version number is in
		header.txt
	"""
	element = {}
	element_list = ['game header', 'header', 'start menu', 'line', 'dash line']
	for i, item in enumerate(element_list):
		temp = 'gui/elements/' + item + '.txt'
		with open(temp, 'r') as fp:
			temp = ''
			for x in fp:
				temp = temp + x
			element[item] = temp
	return element


# tools
def clear():  # clears terminal, re-prints header
	os.system('cls')
	print(element['header'])


# menus
def start_menu():
	clear()
	print(element['start menu'])


element = load_element()  # loads elements on import
