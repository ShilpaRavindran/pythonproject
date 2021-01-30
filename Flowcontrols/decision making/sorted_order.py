num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
num3=int(input("Enter num3"))
if(num1>num2)&(num1>num3):
    if(num2>num3):
        print("sorted order is:",num1,num2,num3)
    else:
        print("sorted order is",num1,num3,num2)
elif(num2>num1)&(num2>num3):
    if(num3>num1):
        print("sorted order is",num2,num3,num1)
    else:
        print("sorted order is",num2,num1,num3)
elif(num3>num1)&(num3>num2):
    if(num1>num2):
        print("sorted order is",num3,num1,num2)
    else:
        print("sorted order is",num3,num2,num1)
elif(num1==num2)&(num2==num3):
    print("3 numbers are equal")
else:
    pass