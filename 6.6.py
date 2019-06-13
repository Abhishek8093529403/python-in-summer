#!/usr/bin/python
'''polling'''
favorite_languages = {'abhishek': 'python','ajaya': 'c++','deshmukh': 'ruby','adya': 'python'}

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

print("\n")

coders = ['abhishek', 'adya', 'ali', 'anshuman', 'sahil', 'abhipsa', 'abhilash']
for coder in coders:
    if coder in favorite_languages.keys():
        print("Thank you for taking the poll, " + coder.title() + "!")
    else:
        print(coder.title() + ", what's your favorite programming language?")
