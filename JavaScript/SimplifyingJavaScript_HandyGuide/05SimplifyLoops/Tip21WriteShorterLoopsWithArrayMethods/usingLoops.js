const prices = ['1.0', '2.15'];
const formattedPrices = [];
for (let i = 0; i < prices.length; i++) {
    formattedPrices.push(parseFloat(prices[i]));
}
console.log(formattedPrices);


const prices = ['1.0', 'negotiable', '2.15'];

const formattedPrices = [];
for (let i = 0; i < prices.length; i++) {
    const price = parseFloat(prices[i]);
    if (price) {
        formattedPrices.push(price);
    }
}
console.log(formattedPrices);
