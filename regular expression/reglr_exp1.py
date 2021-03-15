
from re import *
pattern="ab"
sourse="abababbbab"
matcher=finditer(pattern,sourse)
count=0
for match in matcher:
    print(match.start())
    print(match.group())
    count+=1
print("count=",count)