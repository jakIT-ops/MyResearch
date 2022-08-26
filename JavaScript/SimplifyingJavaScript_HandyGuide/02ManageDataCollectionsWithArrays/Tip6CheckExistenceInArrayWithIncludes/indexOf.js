const sections = ['shipping'];

function displayShipping(sections) {
    if (sections.indexOf('shipping')) {
        return true;
    }
    return false;
}

console.log(displayShipping(sections));

const sections = ['contact', 'shipping'];

function displayShipping(sections) {
    return sections.indexOf('shipping') > -1;
}

console.log(displayShipping(sections));
