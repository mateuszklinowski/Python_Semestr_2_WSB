from sys import argv
import functools
import operator

#script, number,  origin_base, dest_base = argv

def convert_to_decimal(number_list, old_base):

    i = 0
    decimal = 0
    number_list.reverse()
    while i < len(number_list):
        decimal += number_list[i]*old_base**i
        i+=1
    return decimal

def convert_from_decimal(number, new_base):
    rest = number
    remainder = 0
    new_list = []
    while rest != 0 :
        remainder = rest % new_base
        print(remainder)
        rest = rest//new_base
        new_list.append(remainder)
    new_list.reverse()
    return new_list


list = [1,1,0,0,1,0,0]

print(convert_from_decimal(100,2))

print(convert_to_decimal(list,2))



print(red)
