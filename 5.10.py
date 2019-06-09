#!/usr/bin/python
'''no users(If and the lists)'''
current_users = ['abhishek', 'adya', 'admin', 'ajaya', 'anshuman']
new_users = ['abhishek', 'adya', 'deshmukh', 'abhipsa', 'abhilash']

for newuser in new_users:
    if newuser in current_users:
        print("Sorry " + newuser + ", that name is taken.")
    else:
        print("Great, " + newuser + " is still available.")
