num=int(input("enter num:"))#2
pattern=""
sum=0
for i in range(1,(num+1)):#i=1,2
    pattern=str(num)*i
    sum+=int(pattern)
    #print(str(num)*i)#2,22
    #print(str(i),"+",str(i)*i)
    print(pattern)
print("sum is",sum)