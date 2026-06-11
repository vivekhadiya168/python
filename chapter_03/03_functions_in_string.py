# to find length
text = "  hello python  "
print(len(text))

# ends with
print(text.endswith("ivek"))

# starts with
print(text.startswith("viv"))

# starting 1st letter capital  ma lakhva
print(text.capitalize())

# split
print("vivek".split())

# lower() -> Convert to lowercase
print(text.lower())          # hello python

# upper() -> Convert to uppercase
print(text.upper())          # HELLO PYTHON

# strip() -> Remove leading and trailing spaces
print(text.strip())          # hello python

# replace() -> Replace one substring with another
print(text.replace("python", "world"))  # hello world

# split() -> Split string into a list
print("apple,banana,mango".split(","))  # ['apple', 'banana', 'mango']

# join() -> Join list elements into a string
print("-".join(["apple", "banana", "mango"]))  # apple-banana-mango

# find() -> Find index of first occurrence
print("hello".find("e"))    # 1

# startswith() -> Check if string starts with given text
print("hello".startswith("he"))  # True

# endswith() -> Check if string ends with given text
print("hello".endswith("lo"))    # True

# count() -> Count occurrences of a substring
print("hello".count("l"))   # 2

# capitalize() -> Capitalize first letter only
print("hello world".capitalize())  # Hello world

# title() -> Capitalize first letter of every word
print("hello world".title())  # Hello World

# isdigit() -> Check if all characters are digits
print("12345".isdigit())   # True

# isalpha() -> Check if all characters are alphabets
print("Python".isalpha())  # True
