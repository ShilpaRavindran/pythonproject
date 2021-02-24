class Parent:
    def phone(self):
        print("nokia")
    def car(self):
        print("alto")

class Child(Parent):
    def phone(self):
        print("iphone")

ch=Child()
ch.phone()
ch.car()

#3
print()#for new line

class Person():
    def __init__(self,age,name):
        self.age=age
        self.name=name
    def __str__(self):
        return self.name+str(self.age)

p=Person(24,"varun")
print(p)
