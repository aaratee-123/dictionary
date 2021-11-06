dict={"name":"Raju", "marks":56}
var a=require("readline-sync")
var user=a.question("enter the word")
for (i in dict){
    if (i==user){
        console.log("exist")
        break
    }else{
        console.log("not exist")
        break
    }
}

