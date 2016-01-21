#calculate the entropy of a give data set


def entropy(data):
	import math

	total = strong + weak
	ent = -(strong/total)*(math.log((strong/total), 2)) - (weak/total)*(math.log((weak/total), 2))

	return ent

