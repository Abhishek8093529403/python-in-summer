#!/usr/bin/python
'''my pizza, your pizza'''
favorite_pizzas = ['pepperoni', 'mexican', 'panneer']

friend_pizzas = favorite_pizzas.copy()

favorite_pizzas.append("ham")
friend_pizzas.append('cheese')

print("My favorite pizzas are:")
for pizza in favorite_pizzas:
    print("- " + pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print("- " + pizza)
