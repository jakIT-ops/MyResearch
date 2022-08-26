let dad = { name: "Daddy" };
let mom = { name: "Mommy" };

const myMap = new Map();
const myWeakMap = new WeakMap();

myMap.set(dad);
myWeakMap.set(mom);

dad = null;
mom = null;

console.log(myMap);
// Map(1) {{…}}
console.log(myWeakMap);
// WeakMap {}
