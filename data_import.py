
def data_reader(loc):
	import csv
	test_data = []
	with open('data_sets1/test_set.csv', 'rb') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			test_data.append(row)
	return test_data
