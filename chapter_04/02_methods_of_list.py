friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]
print (friends)

# append 
friends.append("vivek")
print(friends)

# sort
l1 = [1,23,45,75,2,5,7,42,6,8]
l1.sort()          # list ne asending order ma sort karse
print(l1)

# reverse
l2 = [1,23,45,75,2,5,7,42,6,8]
l2.reverse()     # list ne reverse karse
print(l2)

# insert
l3 = [1,23,45,75,2,5,7,42,6,8]
l3.insert(2,100)    # index 2 e 100 add karse
print(l3)

# pop
l4 = [1,23,45,75,2,5,7,42,6,8]
value = l4.pop(2)    # index 2 no element delete karse
print(value)        # means je value pop kayri hoy e batavshe
print(l4)             # pop kari ne values return karse

# remove
l5 = [1,23,45,75,2,5,7,42,6,8]
l5.remove(42)         # 42 ne remove karse
print(l5)