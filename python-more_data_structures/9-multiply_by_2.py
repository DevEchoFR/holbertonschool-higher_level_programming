#!/usr/python3
def multiply_by_2(a_dictionary):
    new_dic = {}

    for key in a_dictionary:
        value = a_dictionary[key]
        new_dic[key] = value * 2
    return new_dic
