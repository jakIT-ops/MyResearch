 // 1. 
const constant = 'I am a constant';
constant = " I can't be reassigned";

// Uncaught TypeError: Assignment to constant variable


// 2. 
const person = {
  name: 'Alberto',
  age: 25,
}

person.age = 26;
console.log(person.age);
// 26
