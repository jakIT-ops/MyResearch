//Task: Transform this simple sorting algorithm into a unique sort, meaning that it should not return any duplicate values in the sorted array.

const uniqSort = function(arr) {
    const breadcrumbs = {};
    const result = [arr[0]];
    
    for (let i = 0; i < arr.length; i++) { // start loop at 1 as element 0 can never be a duplicate
        if (!breadcrumbs[arr[i]]) {
            result.push(arr[i]);
            breadcrumbs[arr[i]] = true;
        }
    }
    return result.sort((a, b) => a - b);
};

console.log(uniqSort([4,2,2,3,2,2,2])); // => [2,3,4]