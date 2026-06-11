#  Write a program to find out whether a student has passed or failed if it requires a total of40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

marks1 = int(input("enter marks1 : "))
marks2 = int(input("enter marks2 : "))
marks3 = int(input("enter marks3 : "))

# check for total percentage

total_percentage = ((marks1 + marks2 + marks3)/3)*100

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("you are passed")

else :
    print("you failed. try again next year")