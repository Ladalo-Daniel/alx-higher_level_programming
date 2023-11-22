#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_sum = 0

    gen_set = set()

    gen_set = set(my_list)

    for item in gen_set:
        unique_sum += item

    return (unique_sum)
