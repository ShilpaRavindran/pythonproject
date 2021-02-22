f1=open("teams","r")
f2=open("drop","r")
# lst1=[]
# lst2=[]
# for lines in f1:
#     lst1.append(lines.rstrip("\n"))
#     st1=set(lst1)
#
# print(st1)
#
# for lines in f2:
#     lst2.append(lines.rstrip("\n"))
#     st2=set(lst2)#st2.add(lines.rstrip("\n"))
# print(st2)
#
# q=st1-st2
# print("qualified teams are:",q)

def get_team_set(f):
    st=set()
    for lines in f:
        st.add(lines.rstrip("\n"))
    return st
st1=get_team_set(f1)
st2=get_team_set(f2)
q=st1-st2
print(q)