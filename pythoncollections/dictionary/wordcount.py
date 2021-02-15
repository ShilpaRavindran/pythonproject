txt="hello hi hello hi hello"
words=txt.split(" ")
#print(words)
dict={}
for word in words:
    if word  not in dict:
        dict[word]=1
    else:
        dict[word]+=1
print(dict)
print(dict.get("hello"))
print(max(dict,key=dict.get))
print(sorted(dict,key=dict.get,reverse=True))
# for k,v in dict.items():
#
#     print(v)