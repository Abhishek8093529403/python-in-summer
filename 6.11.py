#!/usr/bin/python
'''cities'''
cities = {
    'berhampur': {
        'country': 'india',
        'population': 6158080,
        'fact': 'silk city'
        },
    'beirut': {
        'country': 'lebanon',
        'population': 8760215,
        'fact': 'city near red sea'
        },
    'manchester': {
        'country': 'united staes',
        'population': 1003285,
        'fact': 'cotton city'
        }
    }

for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    fact = city_info['fact']

    print("\n" + city.title() + " is in " + country + ".")
    print("  It has a population of about " + str(population) + ".")
    print("  Fact : " + fact)
