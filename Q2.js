var a=require("readline-sync")
num=a.questionInt("enter the number")
i=1
d={}
while (i<=num){
    d[i]=i*i
    i++
}console.log(d)