const name = {
    first: 'Lemmy',
    last: 'Kilmister',
};

function getName({ first, last }) {
    return `${first} ${last}`;
}
console.log(getName(name));
