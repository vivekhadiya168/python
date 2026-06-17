# Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute?

class demo:
    a = 4

o = demo()
print(o.a)  # print the class attribute because instance attribute is not present
o.a = 0
print(o.a)   # print the instance attribute because instance attribute is present

print(demo.a)
# aaya class attribute change nai thay. khali instance attribute j set thayo che