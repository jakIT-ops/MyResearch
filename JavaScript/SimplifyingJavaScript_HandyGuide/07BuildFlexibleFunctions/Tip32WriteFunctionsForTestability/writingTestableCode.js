import {getTaxInformation} from "./taxService.js";

function formatPrice(user, { price, location }) {
    const rate = getTaxInformation(location);
    const taxes = rate ? `plus ${price * rate} in taxes.` : 'plus tax.';
    
    return `${user} your total is: ${price} ${taxes}`;
}

const item = { price: 30, location: 'Oklahoma' };
const user = 'Aaron Cometbus';
console.log(formatPrice(user,item));

export { formatPrice };
