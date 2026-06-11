# Write a program to find out whether a given post is talking about “Harry” or not.

post = input("enter the post : ")

if ("harry".lower() in post.lower()):                # harry ne lower ma convert karyu and user je input pe e post ne lower ma convert karyu etle jo koi capital ma HARRY lakhe to pan e lower ma convert thay jay ane show thay
    print("this post is talking about harry")

else : 
    print("this post is not talking about harry")