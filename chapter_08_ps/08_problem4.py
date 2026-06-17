# Write a recursive function to calculate the sum of first n natural numbers.

def sum(n):
    if(n==1):               # aa condition na lagayvi hot to condition infine reverse pan thay
        return 1
    return n + sum(n-1)

n = int(input("enter number : "))
print(sum(n))

