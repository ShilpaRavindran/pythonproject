def add(*args):#*arg accepts as tuples,&**args accepts as dictionary,**kwargs key val.pair
    total=0
    for num in args:
        total+=num
    print(total)

add(10,20,30,40)

def prit_emp_data(**args):
    print(args)
    for k,v in args.items():
        print(k,"->",v)
prit_emp_data(eid=100,job="kakkanad",resid="kannur")