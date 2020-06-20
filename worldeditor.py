import json
import os

def start():
	with open('world_folder/savestate.json.', 'r') as fp:  # loads world from file
			graph = json.load(fp)
	editor_menu(graph, 'start')

def editor_menu(graph, context):
	menu_header()
	keyin = input(' Selection: ')
	if context == 'start':
		if keyin == '1':
			view(graph)
		if keyin == '2':
			menu_header()
			keyin = input(' Enter node name: ')
			edit_node(keyin, graph)
		if keyin == '3':
			node_creation_helper(graph)
		if keyin == 'save':
			with open('world_folder/savestate.json.', 'w') as fp:  # loads world from file
				json.dump(graph, fp)
			print(' Save complete. Press enter to quit or type "continue"')
			keyin = input()
			if keyin == 'continue':
				editor_menu(graph, 'start')

def menu_header():
	os.system('cls')
	print(' ===========+WORLD+EDITOR+====================================================================================')
	print(' 1.view  2.edit node  3.new node || Type "menu" at any time || Type "save" at this menu before closing')
	print(' ----------------------------------------------------------------------------------------')
	print()

def header(string, node='xxx', key='xxx', editor=1):
	os.system('cls')
	print(' ===========+WORLD+EDITOR+====================================================================================')
	print(string,' || Type "menu" at any time || Type "save" at the main menu before closing')
	print(' ----------------------------------------------------------------------------------------')
	if editor == 1:
		print(' Currently editing  Node:',node,'  Key:',key)
		print(' ----------------------------------------------------------------------------------------')
	if editor == 2:
		print(' Currently viewing Node:',node,'  Key:',key)
		print(' ----------------------------------------------------------------------------------------')
	else:
		print()

def nch_header():
	os.system('cls')
	print()
	print(' ===========+N+C+H+====================================================================================')
	print()
	print(' ----------------------------------------------------------------------------------------')
	print()

def view(graph):
	header(' View: graph',editor=0)
	keylist = graph.keys()
	sortkeys = []
	for i in keylist:
		sortkeys.append(i)
	sortkeys = sorted(sortkeys)
	for i, item in enumerate(sortkeys):
		print(' ',i,':',item)
	print()
	x = input(' Press enter to continue...')
	header(' View: select node',editor=0)
	keyin = input(' Select node: ')
	if keyin == 'menu':
		editor_menu(graph, 'start')
	name = keyin
	header(' View: node, keys',node=name, editor=2)
	keylist = graph[keyin].keys()
	sortkeys = []
	for i in keylist:
		sortkeys.append(i)
	sortkeys = sorted(sortkeys)
	for i, item in enumerate(sortkeys):
		print(' ',i,':',item)
	print()
	keyin = input(' Select key, type "back" or "edit": ')
	if keyin == 'menu':
		editor_menu(graph, 'start')
	if keyin == 'back':
		view(graph)
	if keyin == 'edit':
			edit_node(name,graph)
	else:
		header(' View: node key, values',node=name, key=keyin, editor=2)
		for i, item in enumerate(graph[name][keyin]):
			print(' ',i,':',item)
		print()
		keyin = input(' Type "back" or "edit" ')
		if keyin == 'menu':
			editor_menu(graph, 'start')
		if keyin == 'back':
			view(graph)
		if keyin == 'edit':
			edit_node(name,graph)

def edit_node(name, graph):
	header(' Edit: node',node=name, editor=1)
	keylist = graph[name].keys()
	sortkeys = []
	for i in keylist:
		sortkeys.append(i)
	sortkeys = sorted(sortkeys)
	for i, item in enumerate(sortkeys):
		print(' ',i,':',item)
	print()
	keyin = input(' Select key, type "add" or "remove": ')
	if keyin == 'add':
		print(' ----------------------')
		newkey = input(' name of new key: ')
		newvalues = []
		add_key(graph, name, newkey, newvalues)
	if keyin == 'menu':
		editor_menu(graph, 'start')
	if keyin == 'remove':
		remove_key(name, graph)
	else:
		header(' Edit: node key, values',node=name, key=keyin, editor=1)
		for i, item in enumerate(graph[name][keyin]):
			print(' ',i,':',item)
		print()
		keyname = keyin
		keyin = input(' Type "add" or "remove": ')
		if keyin == 'menu':
			editor_menu(graph, 'start')
		if keyin == 'add':
			add_key_value(graph, name, keyname)
		if keyin == 'remove':
			remove_key_value(graph, name, keyname)

def add_key(graph, name, newkey, newvalues):
	header(' Edit: node, keys',node=name, key=newkey, editor=1)
	keyin = input(' Enter values for key (one at a time) type "done" : ')
	if keyin == 'menu':
		editor_menu(graph, 'start')
	if keyin == 'done':
		graph[name][newkey] = newvalues
		edit_node(name, graph)
	else:
		newvalues.append(keyin)
		add_key(graph, name, newkey, newvalues)

def remove_key(name, graph):
	header(' Edit: remove',node=name, editor=1)
	keylist = graph[name].keys()
	sortkeys = []
	for i in keylist:
		sortkeys.append(i)
	sortkeys = sorted(sortkeys)
	for i, item in enumerate(sortkeys):
		print(' ',i,':',item)
	print()
	print(' ----------------------')
	keyin = input(' Select key to remove, or "menu" to cancel: ')
	if keyin == 'menu':
		editor_menu(graph, 'start')
	else:
		print(' ', 'removed key: ', keyin)
		graph[name].pop(keyin)
		print(' ----------------------')
		for i in graph[name]:
			print(' ',i)
		print(' ----------------------')
		keyin = input(' remove another key? Y/N: ')
		if keyin == 'menu':
			editor_menu(graph, 'start')
		if keyin == 'y':
			remove_key(name, graph)
		else:
			edit_node(name, graph)

def add_key_value(graph, name, keyname):
	header(' Edit: node key, values',node=name, key=keyname, editor=1)
	for i, item in enumerate(graph[name][keyname]):
			print(' ',i,':',item)
	print()
	keyin = input(' values (one at a time) type "done" : ')
	if keyin == 'menu':
		editor_menu(graph, 'start')
	if keyin == 'done':
		edit_node(name, graph)
	else:
		graph[name][keyname].append(keyin)
		add_key_value(graph, name, keyname)

def remove_key_value(graph, name, keyname):
	header(' Edit: node key, values',node=name, key=keyname, editor=1)
	for i, item in enumerate(graph[name][keyname]):
			print(' ',i,':',item)
	print()
	keyin = input(' type number you want to remove type "done" : ')
	if keyin == 'menu':
		editor_menu(graph, 'start')
	if keyin == 'done':
		edit_node(name, graph)
	else:
		graph[name][keyname].pop(int(keyin))
		add_key_value(graph, name, keyname)

def node_creation_helper(graph):
	nch_header()
	print(' press 1 for a list of available nodes to connect with')
	print(' press 2 to enter connecting node name')
	keyin = input()
	if keyin == '1':
		keylist = graph.keys()
		sortkeys = []
		for i in keylist:
			sortkeys.append(i)
		sortkeys = sorted(sortkeys)
		for i, item in enumerate(sortkeys):
			print(' ',i,':',item)
		print()
		x = input(' Press enter to continue...')
		node_creation_helper(graph)
	nch_header()
	print(' note: you are choosing the connecting node, not the new node')
	connecting_node_name = input(" Connecting node name:  ")
	print(' Ok, NOW you can choose a new name for your node.')
	print(' All lower case, do not use stupid characters, spaces ARE allowed')
	print(' Special case: IFF a location is a sub-component of an existing node, like the upstairs floor of a building')
	print(' then you will write the prime node name followed by "_" and then the name with NO spaces')
	print(' Example: home_upperfloorhallway')
	print(' -----------------------------------------')
	new_node_name = input(' Enter new node name:  ')
	print(' ',connecting_node_name, ' ..leads to.. ', new_node_name)
	keyin = input(' Is this correct? Y/N:  ')
	if keyin == 'n':
		node_creation_helper(graph)
	nch_header()
	print(' Type general description of new node')
	description = input(' :')
	nch_header()
	d = graph[connecting_node_name]['connected nodes'].append(new_node_name)
	graph[new_node_name] = {"connected nodes": [connecting_node_name], "description": [description], "print name":[], "enter from": [], "exit to": []}
	print(" complete!")
	x = input(' Press Enter...')
	editor_menu(graph, 'start')
