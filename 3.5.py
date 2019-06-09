#!/usr/bin/python
'''guest lists'''
guest = ['Ron Weasley','Harry Potter','Hermione Ranger']
print("Invitation List \n")
message = guest[0] + ", please come to dinner."
print(message)

message1 = guest[1] + ", please come to dinner."
print(message1)

message2 = guest[2] + ", please come to dinner."
print(message2)

print("\n Sorry, " + guest[0] + " can't make it to dinner. \n")

print("New Invitation List \n")


#ron weasley can't make it for dinner. so, call voldemort.

guest[0]="voldemort"

message = guest[0] + ", please come to dinner."
print(message)

message1 = guest[1] + ", please come to dinner."
print(message1)

message2 = guest[2] + ", please come to dinner."
print(message2)
 

