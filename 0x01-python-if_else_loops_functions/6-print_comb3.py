#!/usr/bin/python3
for digit1 in range(0, 9):
    for digit2 in range(digit1 + 1, 9):
        print("{:d}{:d}".format(digit1, digit2), end=", ")
print("{:d}".format(89))
