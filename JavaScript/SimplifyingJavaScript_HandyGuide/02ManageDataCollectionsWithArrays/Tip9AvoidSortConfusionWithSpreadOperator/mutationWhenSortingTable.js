const staff = [
    {
        name: 'Joe',
        years: 10,
    },
    {
        name: 'Theo',
        years: 5,
    },
    {
        name: 'Dyan',
        years: 10,
    },
];

function sortByYears(a, b) {
    if (a.years === b.years) {
        return 0;
    }
    return a.years - b.years;
}

const sortByName = (a, b) => {
    if (a.name === b.name) {
        return 0;
    }
    return a.name > b.name ? 1 : -1;
};

const values = [...staff];
//sorting by years 
values.sort(sortByYears);
//next, sorting by name 
values.sort(sortByName);
//lastly, sorting by years a second time
console.log(values.sort(sortByYears));
