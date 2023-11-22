#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    new_list = []

    element_printed = 0

    try:
        new_list = my_list[:x]

        for item in new_list:
            if isinstance(item, int):
                print("{:d}".format(item), end='')
                element_printed += 1
            else:
                pass

        print()
    except IndexError:
        raise IndexError

    return (element_printed)
