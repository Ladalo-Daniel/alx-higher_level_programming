#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first_char = sentence[0] if length > 0 else "None"
    tup = length, first_char
    return(tup)

vi 9-max_integer.py
#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return ("None")
    x = my_list[0]
    for i in my_list:
        if i > x:
            x = i
    return (x)
