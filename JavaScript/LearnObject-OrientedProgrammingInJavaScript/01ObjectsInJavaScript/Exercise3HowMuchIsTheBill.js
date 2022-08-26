var product = {
    name: 'Cheese',
    price: 20,
    amount: 10,
    madeIn: 'USA',
    //wrtie your function here 
    totalBill() {
        return (this.price*this.amount)
    }
    // totalBill returns 200 dollars.
}