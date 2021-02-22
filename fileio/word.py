f=open("words","r")
lst=[]
dict={}
for lines in f:
    words=lines.rstrip("\n").split(" ")
    lst.append(lines.rstrip("\n"))
    # for word in words:
    #     lst.append(word)
    #     print(word)
# for word in lst:
#     print(word)
    for word in words:
        if word  not in dict:
            dict[word]=1
        else:
            dict[word]+=1
for k, v in dict.items():
    print(k,"==>",v)
print("highest occured word -",max(dict,key=dict.get))
print(sorted(dict,key=dict.get,reverse=True))
print("min",min(dict,key=dict.get))