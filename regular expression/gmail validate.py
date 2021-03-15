

from re import*
rule="[a-zA-Z0-9]{1,64}@gmail.com"

gmail=input("enter a gmail:")
matcher=fullmatch(rule,gmail)
if matcher!=None:
    print("valid gmail")
else:rule="[a-zA-Z0-9]{1,64}@gmail.com"
    print("invalid gmail")