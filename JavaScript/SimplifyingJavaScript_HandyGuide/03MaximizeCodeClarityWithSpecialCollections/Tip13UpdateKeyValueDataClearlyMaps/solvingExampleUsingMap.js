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

let filters = new Map();
filters.set('breed', 'labrador');
console.log(filters);
