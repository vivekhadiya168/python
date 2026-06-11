# methods of tuple

# Creating a tuple
numbers = (10, 20, 30, 20, 40)

# count() -> Counts how many times an element appears
print(numbers.count(20))   # Output: 2

# index() -> Returns the index of the first occurrence
print(numbers.index(30))   # Output: 2

# len() -> Returns the number of elements in the tuple
print(len(numbers))        # Output: 5

# max() -> Returns the largest element
print(max(numbers))        # Output: 40

# min() -> Returns the smallest element
print(min(numbers))        # Output: 10

# sum() -> Returns the sum of all elements
print(sum(numbers))        # Output: 120

# sorted() -> Returns a sorted list from the tuple
print(sorted(numbers))     # Output: [10, 20, 20, 30, 40]

# tuple() -> Converts another iterable into a tuple
list1 = [1, 2, 3, 4]
print(tuple(list1))        # Output: (1, 2, 3, 4)

# Membership operator -> Checks if element exists
print(20 in numbers)       # Output: True
print(50 in numbers)       # Output: False


# Creating tuples
t1 = (10, 20, 30)
t2 = (40, 50, 60)

# Concatenation (+) -> Join two tuples
print(t1 + t2)      # (10, 20, 30, 40, 50, 60)

# Repetition (*) -> Repeat tuple elements
print(t1 * 2)       # (10, 20, 30, 10, 20, 30)

# Indexing -> Access elements
print(t1[0])        # 10
print(t1[-1])       # 30

# Slicing -> Extract a portion of the tuple
print(t1[0:2])      # (10, 20)

# Membership -> Check if element exists
print(20 in t1)     # True
print(100 in t1)    # False

# Loop through tuple
for item in t1:
    print(item)

# Nested tuple
nested = ((1, 2), (3, 4), (5, 6))

# Access inner tuple
print(nested[1])      # (3, 4)

# Access element inside inner tuple
print(nested[1][0])   # 3

# Unpacking tuple values into variables
a, b, c = t1
print(a)            # 10
print(b)            # 20
print(c)            # 30