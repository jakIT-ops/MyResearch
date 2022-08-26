const prices = ['1.0', 'negotiable', '2.15'];
const formattedPrices = prices.map(price => parseFloat(price)) // [1.0, NaN, 2.15]
.filter(price => price);
console.log(formattedPrices);
