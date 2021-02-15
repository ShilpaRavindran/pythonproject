txt="ABAC"
dict={}
for char in txt:
    if char not in dict:
        dict[char]=1
    else:
        #dict[char]+=1
        print(char,"is 1st recursive character")
        break

