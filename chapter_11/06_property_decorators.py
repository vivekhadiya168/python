
class Employee:
    a = 1
    @classmethod                           # aani help thi directly class attribute no use kari shakiye
    def show(cls):                            # @classmethod use kariye to cls lakhvu
        print(f"the class attribute of a is {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = Employee()
e.a = 45

e.name = "vivek ahir"
print(e.fname, e.lname)

e.show()