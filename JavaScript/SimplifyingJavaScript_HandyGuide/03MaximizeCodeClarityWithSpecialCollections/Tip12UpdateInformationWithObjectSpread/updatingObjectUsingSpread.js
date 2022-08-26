const defaults = {
    author: '',
    title: '',
    year: 2017,
    rating: null,
};
const book = {
    author: 'Joe Morgan',
    title: 'ES6 Tips',
};
const bookWithDefaults = { ...defaults, ...book };
console.log(bookWithDefaults);
