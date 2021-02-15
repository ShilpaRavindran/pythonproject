#pairs
lst=[1,2,3,4,5]
no=int(input("enter no:"))
st=set(lst)
out=set()
for num in st:
    op=no-num
    if (op in st) & (op!=num):#op!=num is used to avoid (3,3)
        #print(num,op)
        #break
        if op>num:
            out.add((num,op))
        else:
            out.add((op,num))
print(out)