#!/usr/bin/env python3

from data_import import data_reader
from tree import Tree
import sys

if len(sys.argv)!= 4:
    print("Please add arguments")
    sys.exit(0)
data = data_reader(sys.argv[1])
class_name = data[1]
training_data = data[0]

headers = list(training_data[0].keys())
headers.sort()
headers.remove(class_name)

test_data = data_reader(sys.argv[2])[0]




tree = Tree(training_data, headers, class_name)
tree.save(sys.argv[3])

total = 0
correct = 0
for row in test_data:
    total += 1
    if tree.get_class(row) == row[class_name]:
        correct += 1
print("Percentage correct is: " + str((correct/total)*100) + "%")



# def recurse(data, headers, level):
# 	plus = 0
# 	minus = 0
# 	for dic in data:
# 		if dic['Class'] == 1:
# 			plus += 1
# 		else:
# 			minus += 1
# 	if plus==0:
# 		print("0-line break")
# 	if minus==0:
# 		print("1-line break")

# 	max_gain = 0
# 	zero_set = []
# 	one_set = []
# 	max_header = ''


# 	for header in headers:
# 		gain = information_gain(data, header)
# 		if gain == 1:
# 			print_level(level)
# 			print(header + '1')
# 		elif gain == 0:
# 			print_level(level)
# 			print(header + '0')
# 		if gain[0] > max_gain:
# 			max_gain = gain[0]
# 			zero_set = gain[1]
# 			one_set = gain[2]
# 			max_header = header
# 	print_level(level)
# 	print(max_header + ":", end ="")




# 	recurse(zero_set, headers, level+1)
# 	recruse(one_set, headers, level+1)

# def print_level(level):
# 	for i in range(0, level):
# 		print('\n| ', end="")

# recurse(data, headers, 0)
