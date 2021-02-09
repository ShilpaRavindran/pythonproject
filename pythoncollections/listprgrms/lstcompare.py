#complexity more
# lst1=[10,11,12,13]
# lst2=[10,11,14,15]
# res=[]
# for i in lst1:
#     if i in lst2:
#        res.append(i)
# print(res)

arr1=[10,20,21,22,23]
arr2=[8,9,20,21,25,26]
pos1=0
pos2=0
while((pos1<len(arr1))&(pos2<len(arr2))):
    if(arr1[pos1]==arr2[pos2]):
        print(arr1[pos1])
        pos1+=1
        pos2+=1
    elif(arr1[pos1]>arr2[pos2]):
        pos2+=1
    else:
        pos1+=1

