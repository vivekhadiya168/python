# A file contains a word “Donkey” multiple times. You need to write a program which replaces this word with ##### by updating the same file.

# word = "donkey"

with open("chapter_09_ps/donkey.txt", "r") as f:
    content = f.read()

contentnew = content.replace("donkey", "####")

with open("chapter_09_ps/donkey.txt", "w") as f:
    f.write(contentnew)