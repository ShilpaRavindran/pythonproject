f=open("employee","r")
employees=[]
class Employee:
    def __init__(self,eid,name,desig,sal,exp):
        self.eid=eid
        self.name=name
        self.desig=desig
        self.sal=sal
        self.exp=int(exp)

    def __str__(self):
        return self.name
    def print_details(self):
        print(self.eid,self.name,self.desig,self.sal,self.exp)

for lines in f:
    eid,ename,desig,sal,exp=lines.rstrip("\n").split(",")
    employees.append(Employee(eid,ename,desig,sal,exp))

# for emp in employees:
#     print(emp)
enames=list(map(lambda emp:emp.name.upper(),employees))
print(enames)
devl=(list(filter(lambda emp:emp.desig=="developer",employees)))
name=list(map(lambda name:name.name,devl))
print(name)
expr=(list(filter(lambda emp:emp.exp>2,employees)))
ex=list(map(lambda name:name.name,expr))
print(ex)
qacount=len(list(filter(lambda emp:emp.desig=="qa",employees)))
print(qacount)

high=max(list(map(lambda emp:emp.sal,employees)))
print(high)
#reduce

from _functools import reduce


# salaries=(list(map(lambda emp:emp.sal,employees))
# highsal=reduce(lambda sal1,sal2:sal1 if sal1>sal2 else sal2,salaries)
# print(highsal)
details=[]
details.append((emp.eid,emp.name))






# sal=[]
# for emp in employees:
#     sal.append(emp.sal)
# print(sal)
# print("highest sal",max(sal),ename)
