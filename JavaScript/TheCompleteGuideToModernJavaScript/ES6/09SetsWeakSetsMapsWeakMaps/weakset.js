let dad = {name: "Daddy", age: 50};
let mom = {name: "Mummy", age: 45};

const family = new WeakSet([dad,mom]);

for(const person of family){
  console.log(person);
}
// TypeError: family is not iterable
