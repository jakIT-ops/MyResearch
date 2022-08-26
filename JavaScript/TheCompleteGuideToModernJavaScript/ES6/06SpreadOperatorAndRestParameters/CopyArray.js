const veggie = ["tomato","cucumber","beans"];
const newVeggie = veggie;

// this may seem like we created a copy of the veggie array but look now

veggie.push("peas");
console.log(veggie);
// Array [ "tomato", "cucumber", "beans", "peas" ]

console.log(newVeggie);
// Array [ "tomato", "cucumber", "beans", "peas" ]
