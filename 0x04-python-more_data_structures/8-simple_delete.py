#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):

    if key:
        for dict_key in a_dictionary.keys():
            if dict_key == key:
                del(dict_key)

    else:
        return a_dictionary

    return a_dictionary
