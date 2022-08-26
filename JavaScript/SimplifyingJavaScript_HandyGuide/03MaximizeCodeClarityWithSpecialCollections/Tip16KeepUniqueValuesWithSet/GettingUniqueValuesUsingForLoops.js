const dogs = [
    {
        name: 'max',
        size: 'small',
        breed: 'boston terrier',
        color: 'black'
    },
    {
        name: 'don',
        size: 'large',
        breed: 'labrador',
        color: 'black'
    },
    {
        name: 'shadow',
        size: 'medium',
        breed: 'labrador',
        color: 'chocolate'
    }
]

function getColors(dogs) {
    return dogs.map(dog => dog.color);
}

function getUnique(attributes) {
    const unique = [];
    for (const attribute of attributes) {
        if (!unique.includes(attribute)) {
            unique.push(attribute);
        }
    }
    return unique;
}

const colors = getColors(dogs);
console.log(getUnique(colors));
