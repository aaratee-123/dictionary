#User se 10 students ke naam aur marks lekar unhe ek dictionary me store karaye.
#name=input("enter the name")
#age=int(input("enter the age"))
i=0
dict={}
while i<10:
    name=input("enter the name")
    age=int(input("enter the age"))
    dict.update({name:age})
    i=i+1
print(dict)
    
