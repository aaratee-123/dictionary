#Ek code likhiye jo dictionary ki 3 highest value print karaye. Input :- Output :-
my_dict = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20
    }
t=[]
for x in my_dict.keys():
    if my_dict[x]>50:
        t.append(x)
print(t)