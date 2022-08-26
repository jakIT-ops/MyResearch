const sections = ['contact', 'shipping'];

function displayShipping(sections) {
    return sections.includes('shipping');
}

console.log(displayShipping(sections)); // true
