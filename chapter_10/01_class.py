
class Employee:
    language= "py"             # this is class attribute
    salary = 120000

vivek = Employee()
vivek.name = "harry"           # this is an object(instance) attribute
print(vivek.name, vivek.language, vivek.salary)

rohan = Employee()
rohan.name = "ro ro"
print(rohan.language, rohan.salary)

# here name is object attribute and salary and language are class attributes as they directy belongs to the class
