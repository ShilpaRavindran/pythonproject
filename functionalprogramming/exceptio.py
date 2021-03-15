emps=[
    {"name":"varun","desig":"devop","salary":40000,"join":2000,"resign":2008},
    {"name":"ram","desig":"devop","salary":30000,"join":1983,"resign":1995},
    {"name":"raju","desig":"qa","salary":28000,"join":2004,"resign":2010},
    {"name":"ravi","desig":"qa","salary":32000,"join":2005,"resign":2015},
    {"name":"sravan","desig":"markt","salary":35000,"join":2010,"resign":2020},
]

sal=max(list(map(lambda emp:emp["salary"],emps)))
print(sal)

hiem=list(filter(lambda emp:emp["salary"]==sal,emps))
print(hiem)

exp=list(filter(lambda emp:emp["resign"]-emp["join"]>8,emps))
print(exp)
