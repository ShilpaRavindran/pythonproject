num=int(input("Enter the no:"))
res=0
while(num!=0):
    digit=num%10
    num = num // 10
    res=res+(digit**3)

print(res)
