# "MISSISSIPPI" iss word me har letter ki occurrency count karke ek dictionary me store karaye. 
# Jisme letter dictionary ki keys aur occurrency Uss dictionary ki values hongi. 
 #{M':1,I:4,S:4,P:2} 
a="MISSISSIPPI"
count=0
k={}
for i in a:
    if i not in k:
        k[i]=1
    else:
        k[i]=k[i]+1
print(k)
