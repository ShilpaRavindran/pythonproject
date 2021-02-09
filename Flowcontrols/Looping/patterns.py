# limit=int(input("enter limit:"))
# for i in range(1,limit+1):
#     for j in range(1,i+1):
#         print(i,end="")
#     print("")
#
# limit=int(input("enter limit:"))
# for i in range(1,limit+1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print("")
#
# limit=int(input("enter limit:"))
# for i in range(1,limit+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print("")

for i in range(1,6):
    for j in range(1,10):
        if((i==5)|(i+j==6)|(j-i==4)):
            print("*",end="")
        else:
            print(end=" ")
    print()


