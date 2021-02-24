class Employee:
    c_name="abc"
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def print_person(self):
        print(self.name)
        print(self.age)

emp=Employee("Aadi",23)
print("name:",emp.name,"age:",emp.age)
print(Employee.c_name)