
# Creating a set
s = {10, 20, 30, 40}

# add() -> Add one element
s.add(50)
print(s)

# update() -> Add multiple elements
s.update([60, 70, 80])
print(s)

# remove() -> Remove an element (Error if not found)
s.remove(20)
print(s)

# discard() -> Remove an element (No error if not found)
s.discard(100)
print(s)

# pop() -> Remove a random element
print(s.pop())
print(s)

# copy() -> Create a copy of the set
new_set = s.copy()
print(new_set)

# clear() -> Remove all elements
temp = {1, 2, 3}
temp.clear()
print(temp)   # set()