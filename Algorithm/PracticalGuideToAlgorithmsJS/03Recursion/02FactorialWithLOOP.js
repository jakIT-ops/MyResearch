function computeFactorial(num) {
    var result = 1;

    for(var i = 2; i<= num; i++) {
        console.log(`result = ${result} * ${i} (${result * i})`);
        result *= i;
    }

    return result;
}

console.log(computeFactorial(5));