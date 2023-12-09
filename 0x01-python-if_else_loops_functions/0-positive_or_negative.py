#!/usr/bin/python3
import random
number = random.randint(-10, 10)
print(number, end=" ")

# Check if the number is positive, negative, or zero
if number > 0:
    print("is positive")
if number < 0:
    print("is negative")
else:
    print("zero")
