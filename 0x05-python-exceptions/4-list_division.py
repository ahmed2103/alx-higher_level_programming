def list_division(my_list_1, my_list_2, list_length):
    i = 0
    length = []
    while i < list_length:
        try:
            res = my_list_1[i] / my_list_2[i]
        except (ZeroDivisionError, TypeError, IndexError) as e:
            res = 0
            print(f"Error: {e}")
        else:
            length.append(res)
        finally:
            i += 1
    return length
