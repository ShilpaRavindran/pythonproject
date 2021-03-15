from re import *
#pattern='[abc]'
#pattern='[a-z]'
#pattern='[A-Z]'
#pattern='[a-zA-Z]'
#pattern='[0-9]'
#pattern='[a-zA-Z0-9]'
#pattern='[^0-9]'
#pattern="[^a-zA-Z0-9]"
# pattern="\s"
# pattern="\d"#[0-9]
# pattern="\D"#[^0-9]
#pattern="\w"#[a-zA-Z0-9,_]
pattern="\W"#[^a-zA-Z0-9]

sourse="ab $Zk@9c"
matcher=finditer(pattern,sourse)
#count=0
for match in matcher:
    print(match.start())
    print(match.group())
#     count+=1
# print("count=",count)