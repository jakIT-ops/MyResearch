function removeItem(items, removable) {
    const updated = [];
    for (let i = 0; i < items.length; i++) {
        if (items[i] !== removable) {
            updated.push(items[i]);
        }
    }
    return updated;
}

const items = ['apple', 'banana', 'orange'];
console.log(removeItem(items,'banana'));
