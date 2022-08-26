const capitalize = name => {
    return name[0].toUpperCase() + name.slice(1);
};

const greet = (first, last) => {
    return `Oh, hi ${capitalize(first)} ${capitalize(last)}`;
};

console.log(greet('joe', 'morgan'));
