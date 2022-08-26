function removeItem(items, removable) {
    const index = items.indexOf(removable);
    return [...items.slice(0, index), ...items.slice(index + 1)];
}


const books = ['practical vim', 'moby dick', 'the dark tower'];
const recent = removeItem(books, 'moby dick');
console.log("Recent books: " + recent);
const novels = removeItem(books, 'practical vim');
console.log("Novels: " + novels);
