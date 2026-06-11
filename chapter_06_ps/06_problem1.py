# to find greatest of 4 number enter by use.

a1 = int(input("enter num1 : "))
a2 = int(input("enter num2 : "))
a3 = int(input("enter num3 : "))
a4 = int(input("enter num4 : "))

if(a1>a2 and a1>a3 and a1>a4):
    print("greatest number is a1 : ", a1)

elif(a2>a1 and a2>a3 and a2>a4):
    print("greatest number is a2 : ", a2)

elif(a3>a1 and a3>a2 and a3>a4):
    print("greatest number is a3 : ", a3)

else : 
    print("greatest number is a4 :", a4)