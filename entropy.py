#calculate the entropy of a give data set


def entropy(data):
	import math
	strong = 0
	weak = 0
	for dic in data:
		if dic['Class'] == 1:
			strong += 1
		else:
			weak += 1
	total = strong + weak
	ent = -(strong/total)(math.log((strong/total), 2)) - (weak/total)(math.log((weak/total), 2))

	return ent

