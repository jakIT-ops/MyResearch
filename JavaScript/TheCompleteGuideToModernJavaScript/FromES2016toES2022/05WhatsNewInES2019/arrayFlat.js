const letters = ['a', 'b', ['c', 'd', ['e', 'f']]];
// default depth of 1
console.log(letters.flat());
// ['a', 'b', 'c', 'd', ['e', 'f']]

// depth of 2
console.log(letters.flat(2));
// ['a', 'b', 'c', 'd', 'e', 'f']

// which is the same as executing flat with depth of 1 twice
console.log(letters.flat().flat());
// ['a', 'b', 'c', 'd', 'e', 'f']

// Flattens recursively until the array contains no nested arrays
console.log(letters.flat(Infinity));
// ['a', 'b', 'c', 'd', 'e', 'f']


let greeting = ["Greetings from", " ", "Vietnam"];

// let's first try using a normal `map()` function
greeting.map(x => console.log(x.split(" ")));
// ["Greetings", "from"]
// ["", ""]
// ["Vietnam"]


greeting.flatMap(x => console.log(x.split(" ")))
// ["Greetings", "from", "", "", "Vietnam"]
