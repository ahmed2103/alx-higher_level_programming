def wavg(my_list=[]):
    tws, tw = 0, 0
    for x, y in my_list:
        tws += x * y
        tw += y
    return tws / tw if tw else 0
