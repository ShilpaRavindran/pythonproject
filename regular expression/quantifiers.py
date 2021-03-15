from re import *
#a+ -- check for one or more a
#a* -- a+ + zero no of a(including 0th position)
#a{2}--max 2 a
#a{2,3}--min 2 max 3


pattern="a{2,3}"

matcher=finditer(pattern,"aaacaaaadaabbbaab")
for match in matcher:
    print(match.start())
    print(match.group())
