#!/usr/bin/env python3

from data_import import data_reader
from information_gain import information_gain

data = data_reader("data_sets1/training_set.csv")
print(information_gain(data, 'XB'))