#!/usr/bin/python3
def weight_average(my_list=[]):
    if(my_list):
        return(sum(x*y for x, y in my_list) / sum(y for x, y in my_list))
    else:
        return(0)def complex_delete(a_dictionary, value):
    if value:
        for key, val in list(a_dictionary.items()):
            if val is value:
                del a_dictionary[key]
        return a_dictionary
