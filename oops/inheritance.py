class Parent:
    def phone(self):
        print("inside parents phone methode")

class Child(Parent):
    pass
ch=Child()
ch.phone()