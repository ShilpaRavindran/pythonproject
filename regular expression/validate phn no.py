

from re import*
rule="[+][9][1]\d{10}" #or[0-9]{10}
phnno=input("enter a phno:")
matcher=fullmatch(rule,phnno)
if matcher!=None:
    print("valid")
else:
    print("invalid")
