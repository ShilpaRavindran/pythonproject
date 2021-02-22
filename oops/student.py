class Student:
    def set_std(self,rollno,name,total):
        self.rollno=rollno
        self.name=name
        self.total=total

    def print_std(self):
        print(self.rollno)
        print(self.name)
        print(self.total)

obj=Student()
obj.set_std(1,"Aadi",50)
obj.print_std()

obj1=Student()
obj1.set_std(2,"Anu",45)
obj1.print_std()