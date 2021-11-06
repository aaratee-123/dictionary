// d1 = {'a': 100, 'b': 200, 'c':300}
// d2 = {'a': 300, 'b': 200, 'd':400}
// output should be this: {'a': 400, 'b': 400, 'd': 400, 'c': 300}
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

for (i in d2 ){
    if (i in d1){
        d1[ i ] = d1[ i ] +d2[ i ]
    }
    else{
        d1[ i ] = d2[ i ]
    }
}
console.log(d1)
