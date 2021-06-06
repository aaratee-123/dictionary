# Ek program likhiye jisse ki agar di hui key pehle se dictionary me exist karti ho toh “exists “
# print kare aur agar nahi karti ho toh“not exists” print kare. 
dict={"name":"Raju", "marks":56}
i=input("enter the name")
if i in dict:
    print("exist")
else:
    print("not exist")