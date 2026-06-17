# Repeat program 4 for a list of such words to be censored.

words = ["donkey", "elephent"]

with open("chapter_09_ps/donkey.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))

with open("chapter_09_ps/donkey.txt", "w") as f:
    f.write(content)