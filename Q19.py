# take a list containg only strings. Now, take a string input from user and rearrange 
# the elements of the list according to the number of occurence of the string taken from user 
# in the elements of the list.
# E.g.-LIST : ["no bun","bug bun bug bun bug bug","bunny bug","buggy bug bug buggy"]
# STRING TAKEN : "bug"
# OUTPUT LIST:["bug bun bug bun bug bug","buggy bug bug buggy","bunny bug","no bun"]
list = ["no bun","bug bun bug bun bug bug","bunny bug","buggy bug bug buggy"]
for i in list:
    for j in i:
        list.sort()
    #i=i+1
print(list)