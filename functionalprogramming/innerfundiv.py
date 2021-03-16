def my_div(func):
    def innerFun(num1,num2):
        if num1<num2:
            num1,num2=num2,num1
        return func(num1,num2)
    return innerFun
@my_div
def div(num1,num2):
    return num1/num2
print(div(2,10))