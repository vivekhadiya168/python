
class Employee:
    name = "vivek"
    def show(self):
        print(f"the name is {self.name} and the salary is {self.salary}")


class Programmer(Employee):
    language = "py"
    def showLanguage(self):
        print(f"the name is {self.name} and the language is {self.language}")

a = Employee()
b = Programmer()

print(a.name, b.name,  b.language)

