
class Employee:
    def __init__(self):
        print("constructor of employee :")
    a = 1

class Programmer(Employee):
    def __init__(self):
        print("constructor of Programmer :")
    b = 2

class Manager(Programmer):
    def __init__(self):
        super().__init__()                         # means super() keyword thi parent class ni value pan call karavi shakiye
        print("constructor of Manager :")        # output : constructor of programmer, constructor of manager both
    c = 3

# o = Employee()
# print(o.a)

# p = Programmer()
# print(p.a, p.b)

q = Manager()
print(q.a, q.b, q.c)