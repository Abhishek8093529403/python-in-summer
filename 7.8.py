#!/usr/bin/python
'''deli'''
sandwichorders = ['veggie', 'grilled cheese', 'panner', 'chicken']
finished_sandwiches = []

while sandwichorders:
    current_sandwich = sandwichorders.pop()
    print("I'm working on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")
