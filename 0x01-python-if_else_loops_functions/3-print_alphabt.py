#!/usr/bin/python3
for chars in range(97, 123):
    if chr(chars) != 'q' and chr(chars) != 'e':
        print("{}".format(chr(chars)), end="")
