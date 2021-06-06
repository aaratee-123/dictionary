#Ek dictionary ki value ke sabhi items ko count kijiye jo ki ek list me hai. Input :- Output :-
dict =  {
   'Alex': ['subj1', 'subj2', 'subj3'], 
   'David': ['subj1', 'subj2']}
sum=[]
count=0
for x in dict.values():
    sum=sum+x
print(sum)
i=0
while i<len(sum):
    a=sum[i]
    count=count+1
    i=i+1
print(count)
    #t.update(x)
    #print(t)

