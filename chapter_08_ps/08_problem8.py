# Write a python function to print multiplication table of a given number.

def table(n):
    for i in range (1, n+1):
        print(f"{n} * {i} = {n * i}")
table(5)