class Employee:
    language= "py"
    salary = 120000

    def __init__(self, name, salary, language):                    # dunder method which is automatically call
        self.name = name
        self.salary = salary
        self.language = language
        print("i am creating object")

    def getInfo(self):                 # vivek name no object aapde pass karavyo je accept nata karta etle self lakhyu
        print(f"the language is {self.language}. the salary is {self.salary}")

    @staticmethod                       # jo aapde aa greet mate object pass na karavvo hoy to static method use thay. means greet ne object ni jarur nzthi
    def greet():
        print("good morning")

vivek = Employee("vivek", 130000, "javascript")
# vivek = Employee()
vivek.name = "vivek"
print(vivek.name, vivek.salary, vivek.language)