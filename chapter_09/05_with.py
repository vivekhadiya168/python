
# f = open("chapter_09/file.txt")

# print(f.read())

# f.close()

# the same can be written using with statement like this :

with open("chapter_09/file.txt") as f:
    print(f.read())

# you dont have to close the file