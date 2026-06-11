# negative slicing

name = "vivek"

print(name[0:3])

print(name[-4:-1])  # pachal thi count karse

print(name[1:4])   # negative nu positive number joya che

print(name[:4])    # 1st index ma kai na lakhiye to automatic 0 lay ley. like [0:4]

print(name[1:])    # last index ma kai na lakhiye to automatic last count kari ley. like [1:5]

# skip value in slicing

word = "abcdefghijklmnopqrstuvwxyz"
print(word[0:25:2])                     

# [0:25:2] 
# 0 means starting index
# 25 means ending index
# 2 means ketla skip means ketlo jump marvano che
            