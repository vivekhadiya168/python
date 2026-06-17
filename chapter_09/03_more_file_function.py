
f = open("chapter_09/file.txt")

# lines = f.readlines()              # f.readlines function    lines read kare

# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)

# line3 = f.readline()
# print(line3)

# line4 = f.readline()
# print(line4)

# print(lines, type(lines))
f.close

# 1 1 line read karavvi hoy to f.readline() use karvu 

line = f.readline()                           # aa rite while loop thi pan print karavi shakiye
while (line != ""):
    print(line)
    line = f.readline()