#!/usr/bin/python3

lis_len = 0

my_list = [1, 2, 4, 5]

ele_to_print = 2

element_printed = 0

for ele in my_list:
    lis_len += 1
#    print(my_list[0:ele_to_print])
#    break

new_list = []

new_list = my_list[:ele_to_print]

for item in new_list:
    print(item, end='')

print()
#print("".join(str(my_list[:ele_to_print])))
#print(f"Custom list lenght is {lis_len}")
#print(f"Original len function lenght is {len(my_list)}")
