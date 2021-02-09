##linear search
lst=[10,11,12,13,14]
element=int(input("enter the element:"))
flg=0

for num in lst:
    if(element==num):
        flg=1
        break
    else:
        pass
if(flg==0):
    print("not found")
else:
    print("found")