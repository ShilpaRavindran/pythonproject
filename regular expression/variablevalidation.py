#1st character must be an alphabet a-k
#2nd must be a digit / by 3
#followed by any no. of character


from re import*
rule="[a-kA-K][369][a-zA-Z0-9]*"
variablename=input("enter variable name:")
matcher=fullmatch(rule,variablename)#for exact match
if matcher!=None:
    print("valid variable name")
else:
    print("invalid variable name")


