# #keys id name designtn sal
# print employee name
# empl sal
# chk for gendr key is there if not add gendr key val pair
#iterate all key val pairs

employee={"id":1000,"name":"anu","desig":"qa","salary":30000}
print(employee["name"])
print(employee["salary"])

if "gender" in employee:
    print("gnder exist")
else:
    employee["gender"]="female"
print(employee)

employee["salary"]+=5000
print(employee)

for k in employee:
    print(k,",",employee[k])
print()
for k,v in employee.items():
    print(k,",",v)