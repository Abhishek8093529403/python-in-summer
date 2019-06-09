#!/usr/bin/python
x=["cat","buffalo",5000,False]
print(x)
x[1]="dog" # changing first element of x 
print(x)
bike=["honda","yamaha","suzuki","KTM"]
del bike[1] #deleting the value at index 1 from x
print(bike)
x=["cat","buffalo",5000,False]
x.insert(1,"dog")#its insert the element in given position
print(x)
x.append(True)#it will append the element at last
print(x)
y=x.pop()# list.pop() removes the last item in the list
print("pop",x)
my_list = [0,1,2,3,5,4] # number list
my_list.reverse() # Reverse the items of the list in place
print("Reversed list looks like:", my_list)
my_list.sort(reverse=True) #it will sort list in descending order
print(my_list)
my_list.sort() #it will sort list in ascending order
print(my_list)
mylist=['a','g','d','f','t','x','l']
mylist.sort()
print(mylist)
