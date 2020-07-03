# node.py
"""
placeholder for world node
"""

class Node:
    def __init__(self, data):
        self.name = data['name']
        self.code = data['code']
        self.connections = data['connections']
        self.description = data['description']

    def test(self):
        test_temp = self.data.items()
        for i in test_temp:
            print()
            print(i)
