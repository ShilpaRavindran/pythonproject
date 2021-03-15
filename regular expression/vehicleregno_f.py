from re import *

rule="[K][L]\d{2}[A-Z]{2}\d{1,4}"
f=open("vehicleregno","r")
lst=[]
for lines in f:

    lines=lines.rstrip("\n")
    matcher=fullmatch(rule,lines)
    if matcher!=None:
        f1=lst.append(lines)
print(lst)
