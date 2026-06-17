
class Employee:
    company = "ITC"
    name = "vivek"
    def show(self):
        print(f"the name is {self.name} and the company is {self.company}")

class coder:
    language = "java"
    def printLanguages(self):
        print(f"out of all the languages here is your language: {self.language}")


class programmer(Employee, coder):
    def showLanguage(self):
        print(f"the name is {self.company} and the language is {self.language}")

a = Employee()
b = coder()
c = programmer()

a.show()
b.printLanguages()
c.showLanguage()


print(a.name, b.language, c.language )