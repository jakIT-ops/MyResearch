const fruits = 'Fruits: mango, mangosteen, orange'
const regex = /(mango)/g;

// .exec
RegExp(regex).exec(fruits);
// [
//   'mango',
//   index: 8,
//   input: 'Fruits: mango, mangosteen, orange',
//   groups: undefined
// ]

// matchAll
const matches = [...fruits.matchAll(regex)];
matches[0];
// [
//   'mango',
//   'mango',
//   index: 8,
//   input: 'Fruits: mango, mangosteen, orange',
//   groups: undefined
// ]
