employees={
    1000:{"eid":1000,"ename":"ram","desig":"developer","salary":30000},
    1001:{"eid":1001,"ename":"raj","desig":"qa","salary":28000},
    1002:{"eid":1002,"ename":"roja","desig":"ba","salary":25000}
}
eid=int(input("enter eid:"))
property=(input("enter property:"))
if eid in employees:
    print(employees[eid])#["ename"] to print name also
    if property in employees[eid]:
        print(employees[eid][property])
else:
    print("invalid entry")
