f=open("demo","r")
lst=[]
#st=set()
for lines in f:

    lst.append(lines.rstrip("\n"))#rstip fn. is used to remove \n in right side.
    st=set(lst)
print(lst)
print(st)

