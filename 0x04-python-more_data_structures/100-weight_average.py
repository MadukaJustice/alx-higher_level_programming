#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        num = sum(x * y for x, y in my_list)
        denum = sum(y for x, y in my_list)

    return (num / denum)
