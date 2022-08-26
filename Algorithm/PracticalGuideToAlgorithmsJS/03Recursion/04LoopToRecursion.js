function logNumbers(start, end) {
    
    console.log(`iteratively looping from ${start} until ${end}`);

    for(var i = start; i <= end; i++) {
        console.log('hitting index', i);
    }
}

console.log(`~~~ logNumbers ~~~`);
logNumbers(1,2);

function logNumbersRecursively(start, end) {

    console.log(`recursively looping from ${start} until ${end}`);

    function recurse(i) {
        console.log('hitting index', i);

        if(i < end) {
            recurse(i + 1);
        }
    }

    recurse(start);
}

console.log(`~~~ logNumbersRecursively ~~~`);
logNumbersRecursively(1,3);