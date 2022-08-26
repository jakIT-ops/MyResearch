const defaults = new Map()
    .set('color', 'brown')
    .set('breed', 'beagle')
    .set('state', 'kansas');

const filters = new Map()
    .set('color', 'black');

function applyDefaults(map, defaults) {
    const copy = new Map([...map]);
    for (const [key, value] of defaults) {
        if (!copy.has(key)) {
            copy.set(key, value);
        }
    }
    return copy;
}

console.log(applyDefaults(filters,defaults));
