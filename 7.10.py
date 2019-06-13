#!/usr/bin/python
'''dream vacation'''
nameq = "\nWhat's your name? "
placeq = "If you could visit one place in the world, where would it be? "
continueq = "\nWould you like to let someone else respond? (yes/no) "

# Responses will be stored in the form {name: place}.
responses = {}

while True:
    # Ask the user where they'd like to go.
    name = input(nameq)
    place = input(placeq)

    # Store the response.
    responses[name] = place

    # Ask if there's anyone else responding.
    repeat = input(continueq)
    if repeat != 'yes':
        break

# Show results 
print("\n--- Results ---")
for name, place in responses.items():
    print(name.title() + " would like to visit " + place.title() + ".")
