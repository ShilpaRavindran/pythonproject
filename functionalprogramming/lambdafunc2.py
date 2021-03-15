players=[
    {"name":"sachin","matches":500,"rank":1},
    {"name":"dravid","matches":450,"rank":12},
    {"name":"msd","matches":200,"rank":15},
]

names=list(map(lambda dict:dict["name"],players))
print(names)
#list rank of players
rank=list(map(lambda dict:dict["rank"],players))
print(rank)



#above 300 matchs

match=list(filter(lambda player:player["matches"]>300,players))
print(match)
name=list(map(lambda player:player["name"],match))
print(name)
