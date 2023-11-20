#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    length = []
    for index in range(list_length):
        try:
            res = my_list_1[index] / my_list_2[index]
            length.append(res)
        except ZeroDivisionError:
            res = 0
            print("division by 0")
            length.append(res)
        except TypeError:
            res = 0
            print("wrong type")
            length.append(res)
        except IndexError:
            res = 0
            print("out of range")
            length.append(res)
    return length

