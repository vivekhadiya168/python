# Write a python program using function to convert Celsius to Fahrenheit.

# c = (f-32)*(5/9)

def f_to_c(f):
    c = (f-32)*(5/9)
    return c 

f = int(input("enter temperature in f :"))
c = f_to_c(f)

print(round(c, 2))  # value ne 2 decimal sudhi round of karva
