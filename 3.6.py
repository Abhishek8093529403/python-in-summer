#!/usr/bin/python
'''changing guest lists'''
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

del(guest[0])
guest.insert(0, 'Voldemort')

message = guest[0] + ", please come to dinner."
print(message)

message1 = guest[1] + ", please come to dinner."
print(message1)

message2 = guest[2] + ", please come to dinner."
print(message2)

#we found a bigger table

guest.insert(0, 'Abhishek Pradhan')
guest.insert(1, 'Adya Anwesa Mahapatra')
guest.append('Captain Marvel')

print("\n we found a bigger table. \n")
print("Again New Invitation List \n")


message = guest[0] + ", please come to dinner."
print(message)

message1 = guest[1] + ", please come to dinner."
print(message1)

message2 = guest[2] + ", please come to dinner."
print(message2)

message3 = guest[3] + ", please come to dinner."
print(message3)

message4 = guest[4] + ", please come to dinner."
print(message4)

message5 = guest[5] + ", please come to dinner."
print(message5)
