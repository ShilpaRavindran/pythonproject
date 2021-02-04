num=int(input("enter the number:"))
lowlimit=int(input("enter lower liimit:"))
uplimit=int(input("enter upper limit:"))
for i in range(1,(uplimit+1)):
    if i**num in range(lowlimit,(uplimit+1)):
        print(i**num)