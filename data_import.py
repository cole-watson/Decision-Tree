
def data_reader(loc):
	import csv
	test_data = []
	with open(loc, 'rt') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			row_int = dict((k,int(v)) for k,v in row.items())
			test_data.append(row_int)
	return test_data