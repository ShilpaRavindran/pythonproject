add=lambda no1,no2:no1+no2
print(add(10,30))

sub=lambda no1,no2:no1-no2
print(sub(30,10))

mul=lambda no1,no2:no1*no2
print(mul(20,5))

cube=lambda no1:no1**3
print(cube(3))

div=lambda n1,n2:n1/n2
print(div(10,2))

#map(arg1,arg2)
lst=[1,2,3,4,5]
sq=list(map(lambda no1:no1**2,lst))
print(sq)

names=["ram","raju","ravi"]
up=list(map(lambda name:name.upper(),names))
print(up)

#filter

lst=[1,2,3,4]
evn=list(filter(lambda no:no%2==0,lst))
print(evn)

grtr=list(filter(lambda no:no>2,lst))
print(grtr)