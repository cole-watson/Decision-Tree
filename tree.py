from node import Node

class Tree:

	def __init__(self, data, headers, class_name):
		"""

		:param data: complete dataset to create the decision tree with
		:param headers: the list of attributes in the dataset
		:param class_name: the classification attribute in the dataset
		"""

		self.data = data
		self.headers = headers
		self.root = Node(self.headers, self.data, 0, class_name, None, None, None)

	def __str__(self):

		return str(self.root).lstrip()

	def save(self, loc):
		"""

		:param loc: location to output tree
		:return: Nothing - but saves tree in text format
		"""
		file = open(loc, "wt")

		file.write(self.__str__())

	def get_class(self, row):
		"""

		:param row: the row that needs to be classified
		:return: the classification of the node
		"""
		cur_node = self.root

		while type(cur_node) is not int:
			if row[cur_node.header] == 0:
				cur_node = cur_node.left
			else:
				cur_node = cur_node.right
		return cur_node

		
