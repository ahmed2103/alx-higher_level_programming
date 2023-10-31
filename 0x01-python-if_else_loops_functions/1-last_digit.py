import random

number = random.randint(-10000, 10000)

last = abs(number) % 10

if last > 5:
    comparison = "greater than 5"
elif last < 6 and last != 0:
    comparison = "less than 6 and not 0"
else:
    comparison = "0"

print(f"Last digit of {number} is {last} and is {comparison}")
