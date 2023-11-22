#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []

    element_division = 0


    try:
        if len(my_list_1) != len(my_list_2):
            print("out of range")
        for item_1 in my_list_1:
            for item_2 in my_list_2:
                if isinstance(item_1, int) or isinstance(item_1, float):
                    if isinstance(item_2, int) or isinstance(item_2, float):

                        element_division  = item_1 / item_2
#                        new_list.append(element_division)

                    else:
                        print("wrong type")

                else:
                    print("wrong type")

    except ZeroDivisionError:
        print("division by 0")
    finally:
        new_list.append(element_division)


    return (new_list)
