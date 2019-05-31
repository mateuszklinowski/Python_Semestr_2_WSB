from functools import reduce
import operator


list = [2,2,2,3]

def process_list(list):
    multi = 1
    sum = 0
    for i in list:
        multi = multi * i
        sum = sum + multi
    return sum


print(process_list(list))
