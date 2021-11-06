var a=require("readline-sync")
i=0
d={}
while (i<10){
    let name=a.question("enter the name")
    let age=a.question("enter the age")
    d[name]=age
    i++
}console.log(d)
