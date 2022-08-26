const filters = new Map()
    .set('color', 'black')
    .set('breed', 'labrador');

function sortByKey(a, b) {
    return a[0] > b[0] ? 1 : -1;
}

function getSortedAppliedFilters(filters) {
    const applied = [...filters]
        .sort(sortByKey)
        .map(([key, value]) => {
            return `${key}:${value}`;
        })
        .join(', ');
    return `Your filters are: ${applied}.`;
}

console.log(getSortedAppliedFilters(filters));
