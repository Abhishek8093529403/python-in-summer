#!/usr/bin/python
'''slice out the lists using 4.7.py'''
threemultiples = list(range(3, 31, 3))

for num in threemultiples:
    print(num)

print("The first three items in the list are: ")
print(threemultiples[0:3])

print("\n")

print("The middle four items in the list are: ")
print(threemultiples[3:7])

print("\n")

print("The last three items in the list are: ")
print(threemultiples[7:10])



