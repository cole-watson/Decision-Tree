#!/usr/bin/env python3

from data_import import data_reader
from information_gain import information_gain

data = data_reader("data_sets1/training_set.csv")
headers = list(data[0].keys())
headers.remove("Class")



# cur_data = data

# while True:
# 	for 
