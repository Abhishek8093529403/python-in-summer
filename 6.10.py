#!/usr/bin/python
'''favorite numbers 2'''
favorite_number = {'abhishek': [6,11],'adya': [11,45],'ajaya': [12,87],'abhilash': [50,78],'anshuman': [69,86]}

for name, nums in favorite_number.items():
    print("\n" + name.title() + " likes the following numbers:")
    for number in nums:
        print("  " + str(number))
