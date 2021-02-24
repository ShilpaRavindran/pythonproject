class swift:
    def start(self):
        print("swift starts")
    def accelerate(self):
        print("swift accelerate")
    def stop(self):
        print("swift stop")
class seltos:
    def start(self):
        print("seltos starts")
    def accelerate(self):
        print("seltos accelerate")
    def stop(self):
        print("seltos stop")

class Person:
    def drive(self,car):
        car.start()
        car.accelerate()
        car.stop()

sw=swift()
p=Person()
p.drive(sw)