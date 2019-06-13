#!/usr/bin/python
'''pizza toppings'''
message = "\nWhat topping would you like on your pizza?\nEnter 'quit' when you are finished: "

while True:
    topping = input(message)
    if topping != 'quit':
        print("  I'll add " + topping + " to your pizza.")
    else:
        break
