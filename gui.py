# imports / globals
import os


def load_element():
	"""
	loads element dictionary for easy reference later
	"""
	element = {}
	element_list = ['game header', 'header', 'start menu', 'line', 'dash line']
	for i, item in enumerate(element_list):
		temp = 'text files/' + item + '.txt'
		with open(temp, 'r') as fp:
			temp = ''
			for x in fp:
				temp = temp + x
			element[item] = temp
	return element


def clear():
	os.system('cls')
	print(element['header'])


def menu():
	clear()
	print(element['start menu'])


def display(description, node):
	"""
	parses and displays a description list of strings
	"""
	clear()
	print(element['game header'])
	for i in description:
		print(' ', i)
	print(element['dash line'])
	for i, item in enumerate(node):
		print(' ', i+1, ":", item)
	print()


element = load_element()
