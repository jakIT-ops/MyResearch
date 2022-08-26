class Coupon {
    constructor(price, expiration) {
        this.price = price;
        this.expiration = expiration || 'two weeks';
    }
    getPriceText() {
        return `${this.price}`;
    }
    getExpirationMessage() {
        return `This offer expires in ${this.expiration}.`;
    }
}
const coupon = new Coupon(5);
console.log(coupon.getPriceText());
console.log(coupon.getExpirationMessage());
