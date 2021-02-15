#to find pass students
students={"ajin","abin","akhil","aswin","majo","jino"}
fail={"ajin","majo","aswin"}
diff=students.difference(fail)
print("pass=",diff)

lst=[10,20,"hello",30,50]
lst[1]=60
st=set(lst)
res=list(st)#cant predict the value,bcz sets are not preserved.
print(res[2])