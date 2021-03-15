

from re import*

rule="[0-9]{2}-[0-9]{2}-[0-9]{4}"
date=input("enter a date:")
matcher=fullmatch(rule,date)
if matcher!=None:
    print("valid")
else:
    print("invalid")