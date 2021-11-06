var a=require("readline-sync")
var name=a.question("enter the name")
const list1=[]
let output={}
for (var i of name) {
    if(list1.includes(i)){
        output[i]=output[i]+1

    }else{
        list1.push(i);
        output[i]=1;
    }
}console.log(output)

