function formatPrice(user, { price, location }, getTaxInformation) {
    const rate = getTaxInformation(location);
    const taxes = rate ? `plus ${price * rate} in taxes.` : 'plus tax.';
    return `${user} your total is: ${price} ${taxes}`;
}

const item = { price: 30, location: 'Oklahoma' };
const user = 'Aaron Cometbus';
console.log(formatPrice(user,item,() => null));
console.log(formatPrice(user, item, () => 0.1));

export { formatPrice };
