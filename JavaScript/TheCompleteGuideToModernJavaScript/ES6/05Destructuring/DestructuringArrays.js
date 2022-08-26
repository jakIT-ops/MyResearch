const person = ["Alberto","Montalesi",25];
const [name,surname,age] = person;
console.log(name);
// Alberto


const person = ["Alberto","Montalesi",25];
// we leave out age, we don't want it
const [name,surname] = person;
//the value of age will not be bound to any variable.
console.log(name,surname);
// Alberto Montalesi
