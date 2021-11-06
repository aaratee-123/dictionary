a=[ {"first":"1"}, {"second": "2"}, {"third": "1"}, {"four": "5"}, {"five":"5"}, {"six":"9"}, {"seven":"7"} ]
let list=[];
for (i of a){
    for (x in i){
        if (! list.includes(i[x])){
            list.push(i[x]);
        }
    }
}console.log(list)



