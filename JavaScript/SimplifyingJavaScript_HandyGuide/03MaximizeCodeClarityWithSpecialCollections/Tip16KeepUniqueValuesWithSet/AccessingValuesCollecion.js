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

console.log(getColors(dogs));
