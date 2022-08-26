// create our set
const family = new Set();

// add values to it
family.add("Dad");
console.log(family);
// Set [ "Dad" ]

family.add("Mom");
console.log(family);
// Set [ "Dad", "Mom" ]

family.add("Son");
console.log(family);
// Set [ "Dad", "Mom", "Son" ]

family.add("Dad");
console.log(family);
// Set [ "Dad", "Mom", "Son" ]
