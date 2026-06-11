# Write a program to calculate the grade of a student from his marks from the following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 => C
# 50 – 60 => D
# <50 => F

marks = int(input("enter marks :"))

if (marks<100 and marks >=90):
    print("your grade is : ex")

elif (marks<90 and marks >=80):
    print("your grade is : a")

elif (marks<80 and marks >=70):
    print("your grade is : b")

elif (marks<70 and marks >=60):
    print("your grade is : c")

elif (marks<60 and marks >=50):
    print("your grade is : d")
    
elif (marks<50):
    print("your grade is : f")