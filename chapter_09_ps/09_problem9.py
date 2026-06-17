# Write a program to find out whether a file is identical and matches the content of another file.

with open("chapter_09_ps/donkey.txt") as f:
    content1 = f.read()

with open("chapter_09_ps/poem.txt") as f:
    content2 = f.read()

if(content1 == content2):
    print("files are identical.")

else:
    print("this files are not identical")
