from node import Node

class Tree:

	def __init__(self, data, headers, class_name):
		self.data = data
		self.headers = headers
		self.root = Node(self.headers, self.data, 0, class_name)

	def __str__(self):

		return str(self.root).lstrip()

	def save(self, loc):
		file = open(loc, "wt")

		file.write(self.__str__())

	def get_class(self, row):
		cur_node = self.root

		while type(cur_node) is not int:
			if row[cur_node.header] == 0:
				cur_node = cur_node.left
			else:
				cur_node = cur_node.right
		return cur_node

		
