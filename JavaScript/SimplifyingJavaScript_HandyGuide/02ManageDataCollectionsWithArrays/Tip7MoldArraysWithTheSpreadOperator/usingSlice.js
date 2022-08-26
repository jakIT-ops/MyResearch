function removeItem(items, removable) {
    const index = items.indexOf(removable);
    items.splice(index, 1);
    return items;
}

const items = ['apple', 'banana', 'orange'];
console.log(removeItem(items,'banana'));
