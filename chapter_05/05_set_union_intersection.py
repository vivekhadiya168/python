
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# union() -> Combine both sets
print(A.union(B))          # {1,2,3,4,5,6}

# intersection() -> Common elements
print(A.intersection(B))   # {3,4}

# difference() -> Elements in A but not in B
print(A.difference(B))     # {1,2}

# symmetric_difference() -> Elements not common
print(A.symmetric_difference(B))  # {1,2,5,6}