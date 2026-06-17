# Create a class “Programmer” for storing information of few programmers working at Microsoft.

class Programmer:
    company = "microsoft"                           # company badani same che etle ene e attribute pela j declare kari didho
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("vivek", 1200000, 360020)
print(p.name, p.salary, p.pin, p.company)
