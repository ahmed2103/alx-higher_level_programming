#!/usr/bin/python3

def print_sorted_dictionary(input_dict):
    for key, value in sorted(input_dict.items()):
        print("{}: {}".format(key, value))
