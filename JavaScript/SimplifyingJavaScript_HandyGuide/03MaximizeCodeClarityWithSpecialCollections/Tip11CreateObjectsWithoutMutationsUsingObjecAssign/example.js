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

function addBookDefaults(book, defaults) {
    return Object.assign(defaults, book);
}

console.log(addBookDefaults(book,defaults));
