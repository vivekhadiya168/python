
marks = {
    "vivek": 100,        
    "jay": 56,
    "shubham": 23
}

# .items
print(marks.items())  # dictionary ni badhi item print karavse

# .keys()
print(marks.keys())     # badhi keys aapse

# .values()
print(marks.values())

# update()
marks.update({"vivek": 99, "harry": 99})      # update karva   je nai hoy e add thay jase. ex : aaya harry and ena marks add thay jase
print(marks)

# get()
print(marks.get("vivek"))
# print(marks.get("vivek1"))      # aa use kariye ne key exist na karti hoy to none malse
# print(marks["vivek1"])          # aa use kariye ne key exist na karti hoy to error malse

# clear()                          # dictionary ne khali kari nake
# marks.clear()
# print(marks)

# copy()
mm = marks.copy()
# print(marks)
# print(mm)

# pop
marks.pop("harry")
print(marks)