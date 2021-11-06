
// recursion example of function

function sum(num){
    if (num==1){
        return 1
    }else{
        return(num+(sum(num-1)))
    }
}
const a=require("readline-sync")
var num=a.questionInt("enter the number")
var c=sum(num)
console.log(c)