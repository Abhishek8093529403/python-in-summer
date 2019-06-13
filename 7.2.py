#!/usr/bin/python
'''restaurant seating'''
party_size = input("How many people are in your dinner party tonight? \n")
partysize = int(party_size)

if partysize > 8:
    print("I'm sorry, you'll have to wait for a table.")
else:
    print("Your table is ready.")
