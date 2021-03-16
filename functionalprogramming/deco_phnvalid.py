def validphn(fun):
    def innerFun(phn):
        if len(phn)<10:
            raise Exception("invalid")
        else:
            return fun(phn)
    return innerFun
@validphn
def valphn(phn):
    return "valid"+phn
print(valphn("1234567890"))
