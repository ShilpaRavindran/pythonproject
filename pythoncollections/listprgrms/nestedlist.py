employees=[
    [100,"Tom","developer",25000],
    [101,"Jack","qa",28000],
    [102,"Rose","developer",25000],
    [103,"Quin","se",30000]
]
sum=0
for employee in employees:
    print(employee[1])
for developer in employees:
    if(developer[2]=="developer"):
        print(developer)
for employee in employees:
    sum=sum+employee[3]
print(sum)

# sallst=[]
# for employee in employees:
#     sallst.append(employee[3])
# print("high sal=",max(sallst))
high=0
for employee in employees:
    if(employee[3]>high):
        high=employee[3]
print(high)


