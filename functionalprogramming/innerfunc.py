def my_sub(func):
    def innerFun(num1,num2):
        if num1<num2:
            num1,num2=num2,num1
        return func(num1,num2)
    return innerFun
@my_sub
def sub(num1,num2):
    return num1-num2
print(sub(10,20))