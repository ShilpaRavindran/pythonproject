limit=int(input("enter the limit:"))
i=1
osum=0
esum=0
while(i<=limit):
    if(i%2==0):
        esum+=i
    else:
        osum+=i
    i+=1

print(esum)
print(osum)
