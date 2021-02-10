arr=[1,2,3,4]
sum=7
low=0
upp=len(arr)-1
while(low<upp):
    total=arr[low]+arr[upp]
    if(sum==total):
        print(arr[low],arr[upp])
        low+=1
        upp+=1
        break
    elif(total>sum):
        upp-=1
    elif(total<sum):
        low+=1

