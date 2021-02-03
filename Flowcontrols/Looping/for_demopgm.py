#for i in range(10,0,-1):
#    print(i)
#limit=int(input("enter the limit:"))
#for i in range(1,(limit+1)):
#    print(i**2)
num=int(input("enter num:"))
flg=0
for i in range(2,num):
    if(num%i==0):
        flg=1
        break
    else:
        flg=0
if(flg==0):
    print("prime")
else:
    print("not prime")