#!/usr/bin/python
'''multiples of 10'''
number = input("Give me a number, please: ")
num = int(number)

if num % 10 == 0:
    print(str(number) + " is a multiple of 10.")
else:
    print(str(number) + " is not a multiple of 10.")
