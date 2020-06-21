# parser

def description(graph):  ### can be moved and consolidated, par. will handle string operations in the future
	description = graph['pos']['description']
	return description

def nodes(graph):
	node = graph['pos']['connected nodes']
	return node