#!/usr/bin/python3

def best_score(a_dictionary):

    if not a_dictionary:
        return None

    def max_score(values=[]):
        if not values:
            return None

        max_val = values[0]  # Set the first item as the max value.

        for score in values:
            if score > max_val:
                max_val = score

        return (max_val)

    value_list = []

    for k, v in a_dictionary.items():
        value_list.append(v)

    highest_score = max_score(value_list)

    best_score_key = ""

    for key, value1 in a_dictionary.items():
        if highest_score == value1:
            best_score_key = key

    return best_score_key
