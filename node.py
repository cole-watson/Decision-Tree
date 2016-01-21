
import math
class Node:



	def __init__(self, headers, sub_data, level):
		self.level = level
		self.sub_data = sub_data
		self.zero_data = []
		self.one_data = []
		self.headers = headers
		self.header = self.get_header()
		for row in sub_data:
			if row[self.header] == 0:
				self.zero_data.append(row)
			elif row[self.header] == 1:
				self.one_data.append(row)
		self.headers.remove(self.header)
		self.left = self.compute_left()
		self.right = self.compute_right()


	def __str__(self):
		final = '\n'
		for i in range(0, self.level):
			final += "| "
		final += self.header +  " = 0 : "
		final += str(self.left)
		if type(self.left) is int:
			final += "\n"


		for i in range(0, self.level):
			final += "| "
		final += self.header +  " = 1 : "
		final += str(self.right)
		if type(self.right) is int:
			final += "\n"


		return final

	def compute_left(self):
		zero = 0
		one = 0

		for row in self.zero_data:
			if row["Class"] == 0:
				zero += 1
			elif row["Class"] == 1:
				one += 1
		if zero == 0:
			return 1
		if one == 0:
			return 0
		if self.headers==[]:
			print(self.header +" : " + str(self.headers))
			if zero>one:
				return 0
			else:
				return 1



		return Node(self.headers, self.zero_data, self.level+1)
		

	def compute_right(self):
		zero = 0
		one = 0

		for row in self.one_data:
			if row["Class"] == 0:
				zero += 1
			elif row["Class"] == 1:
				one += 1
		if zero == 0:
			return 1
		if one == 0:
			return 0
		if self.headers==[]:
			print(self.header +" : " + str(self.headers))
			if zero>one:
				return 0
			else:
				return 1

		return Node(self.headers, self.one_data, self.level+1)

	def get_header(self):

		max_gain = 0
		max_header = ''



		for header in self.headers:
			gain = self.information_gain(self.sub_data, header)
			if gain > max_gain:
				max_gain = gain
				max_header = header
		return max_header


	def entropy(self, data):
		zero = 0
		one = 0

		for row in data:
			if row["Class"] == 0:
				zero += 1
			elif row["Class"] == 1:
				one += 1
		total = zero+one
		if zero==0 or one == 0:
			return 0

		ent = -(one/total)*(math.log((one/total), 2)) - (zero/total)*(math.log((zero/total), 2))

		return ent

	def information_gain(self, data, header):
		e = self.entropy(data)
		_zero_data = []
		_one_data = []
		s = len(data)
		s_0 = 0
		s_1 = 0

		for row in data:
			if row[header] == 0:
				_zero_data.append(row)
				s_0 += 1
			else:
				_one_data.append(row)
				s_1 += 1

		return (e-(s_0/s)*self.entropy(_zero_data)-(s_1/s)*self.entropy(_one_data))



