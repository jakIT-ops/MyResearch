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


function getDogNames(dogs, filterFunc) {
    return dogs
        .filter(filterFunc)
        .map(dog => dog.name)
}

console.log(getDogNames(dogs, dog => dog.weight < 20));
