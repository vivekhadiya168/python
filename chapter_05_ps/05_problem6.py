# create an empty dictionary. allow 4 friends to enter their favourite language as value and use keys as their names. assume that the names are unique.

d = {}

name = input("enter friend name : ")
lang = input("enter favourite language name : ")

d.update({name : lang})

name = input("enter friend name : ")
lang = input("enter favourite language name : ")

d.update({name : lang})

name = input("enter friend name : ")
lang = input("enter favourite language name : ")

d.update({name : lang})

name = input("enter friend name : ")
lang = input("enter favourite language name : ")

d.update({name : lang})

print(d)