#Ek program likhiye jo dictionary me se duplicate keys hata de. 
 
dic={
    "ball":"red",
    "bat":4,
    "wickets":8,
    "ball":"green",
    "bat":3
    } 
dict1={}
for x,y in dic.items():
    j=x
    if x==j:
        print(dic)
        break
