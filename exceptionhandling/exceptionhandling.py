#ubnormal code-exception
#divided by 0,index,
#try,except,finally use as keywords ,these are  blocks
#try:
#   doubtful code
#except:
#   handling code
#finally:
#   clean up processing code

no1=int(input("enter no1"))
no2=int(input("enter no2"))
try:
    res=no1/no2
    print(res)
except Exception as e:
    no2 = int(input("enter no2"))
    res = no1 / no2
    print(res)
finally:
    print("database operation")
    print("file write")
