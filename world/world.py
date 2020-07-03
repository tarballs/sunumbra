# world.py
import json
from world import chunk

global graph


def test():
	chunk.test()


def load():
	with open('saves/testworld/chunk0001.json.', 'r') as fp:  # loads world from file
		graph = json.load(fp)
	return graph


def save():
	with open('jsonfiles/savestate.json', 'w') as fp:
		json.dump(graph, fp)


def add_chunk():
	"""adds chunk to existing world, calls chunk.new_chunk()"""
	pass
