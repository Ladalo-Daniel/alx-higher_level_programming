#!/usr/bin/python3

def common_elements(set_1, set_2):
    new_set = set()

    common_items = []

    for item_1 in set_1:
        for item_2 in set_2:
            if item_1 == item_2:
                common_items.append(item_1)

    new_set = set(common_items)

    return (new_set)
