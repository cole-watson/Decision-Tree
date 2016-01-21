

def information_gain(data, val):
	from entropy import entropy
	e = entropy(data)
	zero_data = []
	s = len(data)
	s_0 = 0
	one_data = []
	s_1 = 0
	for row in data:
		if row[val] == 0:
			zero_data.append(row)
			s_0 += 1
		else:
			one_data.append(row)
			s_1 += 1
	return (e-(s_0/s)*entropy(zero_data)-(s_1/s)*entropy(one_data))
