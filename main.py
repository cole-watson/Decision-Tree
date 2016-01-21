#!/usr/bin/env python3

from data_import import data_reader
from tree import Tree
import sys

if len(sys.argv)!= 4:
    print("Please add arguments")
    sys.exit(0)


def main():
    data = data_reader(sys.argv[1])
    training_data = data[0]
    class_name = data[1]

    headers = list(training_data[0].keys())
    headers.remove(class_name)
    headers.sort()

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


if __name__ == "__main__":
    main()
