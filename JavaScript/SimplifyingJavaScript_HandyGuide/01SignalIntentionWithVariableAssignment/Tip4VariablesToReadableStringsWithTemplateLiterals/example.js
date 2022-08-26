function getProvider() {
    return 'pragprog.com/cloud';
}

function generateLink(image, width) {
    const widthInt = parseInt(width, 10);
    return 'https://' + getProvider() + '/' + image + '?width=' + widthInt;
}

const image = 'foo';
const width = 200.5;
console.log(generateLink(image,width));
