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


const filters = {
      color: 'brown',
};

function addFilters(filters, key, value) {
    filters[key] = value;
}

function deleteFilters(filters, key) {
    delete filters[key];
}

function clearFilters(filters) {
    filters = {};
    return filters;
}

console.log("Addiing a filter:");
addFilters(filters,'size','large');
console.log(filters);
console.log("Deleting a filter:");
deleteFilters(filters,'color');
console.log(filters);
console.log("Clearing filters:");
console.log(clearFilters(filters));
