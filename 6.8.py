#!/usr/bin/python
'''pets'''
# Make an empty list
pets = []

# Make individual pets dictionary
pet = {
    'animal type': 'cat',
    'name': 'muffin',
    'owner': 'adya',
    'weight': '2.3 kg',
    'eats': 'milk',
}
pets.append(pet)

pet = {
    'animal type': 'chicken',
    'name': 'kukudu ku',
    'owner': 'abhilash',
    'weight': '2.8 kg',
    'eats': 'seeds',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'lol',
    'owner': 'abhishek',
    'weight':'9.35 kg',
    'eats': 'pedigree',
}
pets.append(pet)

# Display information about each pet.
for pet in pets:
    print("\nHere's what I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))
