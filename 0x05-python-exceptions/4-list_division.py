#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []

    element_divison = 0

    for item in range(list_length):
        try:
            element_division = my_list_1[item] / my_list_1[item]

        except ZeroDivisionError:
            print("division by 0")
#            element_division = 0
            pass
        except TypeError:
            print("wrong type")
#            element_division = 0
            pass
        except IndexError:
            print("out of range")
#            element_division = 0
            pass
        finally:
            new_list.append(element_division)

    return (new_list)
