class pycharm:
    def create_file(self):
        print("pycharm create file")

    def exicute_file(self):
        print("pycharm exicutes")


class vsstudio:
    def create_file(self):
        print("vsstudio create file")

    def exicute_file(self):
        print("vsstudio exicutes")

class Programmer:
    def codding(self,ide):
        ide.create_file()
        ide.exicute_file()

cd=vsstudio()
p=Programmer()
p.codding(cd)

