var mainString="My name is kumar, and my friend’s name is Dhamu" 
var subString="is"
a=mainString.split(" ")
// console.log(a)
count=0
for (i in a){
    n=a[i]
    if (n==="is"){
        count=count+1
    }
}console.log(count)
