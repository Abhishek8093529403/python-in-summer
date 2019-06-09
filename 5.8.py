#!/usr/bin/python
'''hello admin(If and the lists)'''
usernames = ['abhishek', 'adya', 'admin', 'ajaya', 'anshuman']

for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + username + ", thank you for logging in again!")
