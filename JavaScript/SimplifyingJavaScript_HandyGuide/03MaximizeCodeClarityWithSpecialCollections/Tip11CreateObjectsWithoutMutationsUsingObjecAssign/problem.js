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

const anotherBook = {
    title: 'Another book',
    year: 2016,
};

function addBookDefaults(book, defaults) {
    return Object.assign(defaults, book);
}


console.log("Using book: ");
console.log(addBookDefaults(book,defaults));
console.log("\n");
console.log("Using another book: ");
console.log(addBookDefaults(anotherBook,defaults));
