#!/ussr/bin/python3

def roman_to_int(roman_string):

    if not isinstance(roman_string, str) or not roman_string:
        return 0

    rom_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    int_val = 0

    prev_value = 0

    for char in reversed(roman_string):
        value = rom_dic.get(char, 0)

        if value < prev_value:
            int_val -= value
        else:
            int_val += value

        prev_value = value

    return int_val
