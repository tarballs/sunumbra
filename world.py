import json

def load():
	global graph
	with open('jsonfiles/savestate.json.', 'r') as fp:  # loads world from file
		graph = json.load(fp)
	return graph

def getpos():
	pos = graph['pos']
	return pos

def setpos(node_name):
	graph['pos'] = graph[node_name]

def save():
	with open('jsonfiles/savestate.json', 'w') as fp:
		json.dump(graph, fp)
