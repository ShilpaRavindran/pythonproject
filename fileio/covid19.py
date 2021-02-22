f=open("covid_19_india(1).csv","r")
dict={}
s={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    state=data[3]
    confirmed=int(data[-1])
    cured=int(data[-3])
    death=int(data[-2])
    dict[data]={state:{"state":state,"confirmed":confirmed,"death":death,"cured":cured}}

print(dict)
