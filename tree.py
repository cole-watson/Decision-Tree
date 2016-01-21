from node import Node

class Tree:

	def __init__(self, data, headers):
		self.data = data
		self.headers = headers
		self.root = Node(self.headers, self.data, 0)

	def __str__(self):

		return str(self.root).lstrip()

	def save(self, loc):
		file = open(loc, "wt")

		file.write(self.__str__())
