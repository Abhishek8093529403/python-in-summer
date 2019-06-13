#!/usr/bin/python
'''no pastrami'''
sandwichorders = [
    'pastrami', 'veggie', 'grilled cheese', 'pastrami',
    'paneer', 'chicken', 'pastrami']
finished_sandwiches = []

print("I'm sorry, we're all out of pastrami today.")
while 'pastrami' in sandwichorders:
    sandwichorders.remove('pastrami')

print("\n")
while sandwichorders:
    current_sandwich = sandwichorders.pop()
    print("I'm working on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")
