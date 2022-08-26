const dogs = [
    {
        name: 'max',
        weight: 10,
        breed: 'boston terrier',
        state: 'wisconsin',
        color: 'black',
    },
    {
        name: 'don',
        weight: 90,
        breed: 'labrador',
        state: 'kansas',
        color: 'black',
    },
    {
        name: 'shadow',
        weight: 40,
        breed: 'labrador',
        state: 'wisconsin',
        color: 'chocolate',
    },
];


const identity = field => value => dog => dog[field] === value;
const colorCheck = identity('color');
const stateCheck = identity('state');
console.log(getDogNames(dogs, colorCheck('chocolate')));
console.log(getDogNames(dogs, stateCheck('kansas')));
