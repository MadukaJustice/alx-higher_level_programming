#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if len(my_list) == 0:
        return
    my_list.reverse()
    for i in my_list:
        print("{:d}".format(i))

'''
ALTERNATE SOLUTION (NOT OPTIMIZED)
def print_reversed_list_integer(my_list=[]):
    for i in range(len(my_list)):
        if i == (len(my_list)):
            print()
        while i < (len(my_list)):
            print('{:d}'.format(my_list[i-1]))
            i -= 1
'''
