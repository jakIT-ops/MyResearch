const defaults = {
    author: '',
    title: '',
    year: 2017,
    rating: null,
};
const book = {
    author: 'Joe Morgan',
    title: 'Simplifying JavaScript',
};

const updated = Object.assign({}, defaults, book);
console.log(`Updated object:`);
console.log(updated);
console.log("\n");

console.log(`Original object:`);
console.log(defaults); 
