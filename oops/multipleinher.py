class Parent:
    def m1(self):
        print("inside m1")

class SubChild():
    def m1(self):
        print("inside m2")
class Child(SubChild,Parent):
    def m3(self):
        print("inside m3")

ch=Child()
ch.m3()
# ch.m2()
ch.m1()