#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    new_list = []

    num_of_element = 0

    try:
        new_list = my_list[:x]

        for item in new_list:
            print(item, end='')
            num_of_element += 1
        print()
#        num_of_element = lis_len(new_list)

    except Exception as e:
        pass

    return num_of_element
