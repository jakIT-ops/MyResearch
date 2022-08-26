const myObj = {
  name: "Alberto",
  age: 25,
  greet() {
    console.log("hello");
  },
}
console.log(Object.getOwnPropertyDescriptors(myObj));
// age:{value: 25, writable: true, enumerable: true, configurable: true}

// greet:{value: ƒ, writable: true, enumerable: true, configurable: true}

// name:{value: "Alberto", writable: true, enumerable: true, configurable: true}
