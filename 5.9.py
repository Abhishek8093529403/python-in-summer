#!/usr/bin/python
'''no users(If and the lists)'''
usernames = ['abhishek', 'adya', 'admin', 'ajaya', 'anshuman']

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello " + username + ", thank you for logging in again!")
else:
    print("We need to find some users!")

print("\nIn case of no users present")

usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello " + username + ", thank you for logging in again!")
else:
    print("We need to find some users!")
