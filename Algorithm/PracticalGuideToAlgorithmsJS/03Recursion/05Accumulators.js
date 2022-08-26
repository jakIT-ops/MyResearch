function joinElements(array, joinString) {

    function recurse(index, resultSoFar) {
        resultSoFar += array[index];

        if(index === array.length - 1) {
            return resultSoFar;
        } else {
            return recurse(index + 1, resultSoFar + joinString);
        }
    }

    return recurse(0, '');
}

console.log(joinElements(['s', 'cr', 't cod', ' :) :)'], 'e'));