#!/usr/bin/python
'''people'''
#a empty list of people
people=[]
person = {'first_name': 'Abhishek','last_name': 'Pradhan','age': 20,'city': 'Berhampur'}
people.append(person)
person = {'first_name': 'Adya','last_name': 'Mahapatra','age': 19,'city': 'Bhubaneswar'}
people.append(person)
person = {'first_name': 'Abhilash','last_name': 'Loi','age': 19,'city': 'Boudh'}
people.append(person)
# Display all of the information in the dictionary.
for person in people:
    name = person['first_name'] + " " + person['last_name']
    age = str(person['age'])
    city = person['city'].title()
    
    print(name + ", of " + city + ", is " + age + " years old.")
