class Parent:
    def m1(self):
        print("inside m1")
class SubChild(Parent):
    def m2(self):
        print("inside m2")
class Child(SubChild):
    def m3(self):
        print("inside m3")

ch=Child()
ch.m3()
ch.m2()
ch.m1()

sb=SubChild()
sb.m1()
sb.m2()

p=Parent()
p.m1()