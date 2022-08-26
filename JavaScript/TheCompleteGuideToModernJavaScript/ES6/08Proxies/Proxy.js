// our object
const dog = { breed: "German Shephard", age: 5}

// our Proxy
const dogProxy = new Proxy(dog, {
  get(target,breed){
    return target[breed].toUpperCase();
  },
  set(target, breed, value){
    console.log("changing breed to...");
    target[breed] = value;
  }
});

console.log(dogProxy.breed);
// "GERMAN SHEPHARD"
console.log(dogProxy.breed = "Labrador")
// changing breed to...
// "Labrador"
console.log(dogProxy.breed);
// "LABRADOR"
