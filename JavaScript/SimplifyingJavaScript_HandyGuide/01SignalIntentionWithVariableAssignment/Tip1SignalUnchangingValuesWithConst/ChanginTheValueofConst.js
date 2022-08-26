const discountable = [];
const cart = [
    {
        item: 'Book',
        discountAvailable: false,
    },
    {
        item: 'Magazine',
        discountAvailable: true,
    },
];
// Skip some lines
for (let i = 0; i < cart.length; i++) {
    if (cart[i].discountAvailable) {
        discountable.push(cart[i]);
    }
}
console.log(discountable);
