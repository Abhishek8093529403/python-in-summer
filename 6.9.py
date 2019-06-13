#!/usr/bin/python
'''favorite_places'''
favorite_places = {
    'abhishek': ['switzerland', 'death valley', 'eiffel tower'],
    'adya': ['hawaiin', 'sweden'],
    'loibhaina': ['mt everest', 'boudh', 'goa']
    }

for name, places in favorite_places.items():
    print("\n" + name.title() + " likes the following places:")
    for place in places:
        print("- " + place.title())
