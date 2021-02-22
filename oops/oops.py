
class Person:
    def set_person(self,age,name):
        self.name=name
        self.age=age
    def print_person(self):
        print(self.name)
        print(self.age)

obj=Person()
obj.set_person(24,"anu")
obj.print_person()

obj1=Person()
obj1.set_person(25,"jack")
obj1.print_person()

obj3=Person()
obj3.set_person(23,"naina")
obj3.print_person()