#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):

    key_list = []

    for key in a_dictionary.keys():
        key_list.append(key)

    key_list = sorted(key_list)

    for item in key_list:
        print("{}: {}".format(item, a_dictionary[item]))
