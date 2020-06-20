"""manager class, contains data for everything else"""
import world, gui, par
import worldeditor

def start():
	gui.menu()
	controller('menu')

def controller(context):
	keyin = gui.getinput()
	if context == 'menu':
		if keyin == '1':
			gui.clear()
			#placeholder for world selection, then call world.load with name
			global graph
			graph = world.load()
			rungame()
		if keyin == '3':
			graph = worldeditor.start()
		else:
			print('Input not recognized')
			controller(context)
	if context == 'game':
		node = par.nodes(graph)
		lengthnode = len(node)
		if keyin == '1' and lengthnode >= 1:
			world.setpos(node[0])
			rungame()
		if keyin == '2' and lengthnode >= 2:
			world.setpos(node[1])
			rungame()
		if keyin == '3' and lengthnode >= 3:
			world.setpos(node[2])
			rungame()
		if keyin == '4' and lengthnode >= 4:
			world.setpos(node[3])
			rungame()
		else:
			print('Input not recognized')
			controller(context)

def rungame():
	description = par.description(graph)
	node = par.nodes(graph)
	gui.display(description, node)
	controller('game')
