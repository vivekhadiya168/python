# Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.

with open("chapter_09_ps/poem.txt") as f:
    c = f.read()
    if ("twinkle" in c):
        print("the word twinkle is present in content")
    
    else:
        print("the word twinkle is present in content")
