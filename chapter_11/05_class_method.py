
class Employee:
    a = 1
    @classmethod                           # aani help thi directly class attribute no use kari shakiye
    def show(cls):                            # @classmethod use kariye to cls lakhvu
        print(f"the class attribute of a is {cls.a}")

e = Employee()
e.a = 45

e.show()

# aaya a ni value instance attribute ni value 45 aavat pan aapde classmethod no use karyo etle class attribute ni valur show karse
