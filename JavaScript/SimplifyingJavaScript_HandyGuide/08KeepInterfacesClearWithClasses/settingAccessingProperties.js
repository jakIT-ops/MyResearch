class Coupon {
    constructor(price, expiration) {
        this.price = price;
        this.expiration = expiration || 'two weeks';
    }
}
const coupon = new Coupon(5);
console.log(coupon.price);
console.log(coupon['expiration']);

