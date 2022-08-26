// regex that matches any character in the range from 'a' to 'd'
const regEx = /[a-d]/g;
const str = "Lorem ipsum dolor sit amet"
const regExIterator = str.matchAll(regEx);

console.log(Array.from(regExIterator));
// [
//     ["d", index: 12, input: "Lorem ipsum dolor sit amet", groups: undefined]
//     ["a", index: 22, input: "Lorem ipsum dolor sit amet", groups: undefined]
// ]
