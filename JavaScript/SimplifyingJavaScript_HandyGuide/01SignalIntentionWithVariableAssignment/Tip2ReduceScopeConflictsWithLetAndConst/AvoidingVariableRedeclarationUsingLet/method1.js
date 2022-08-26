function getLowestPrice(item) {
    let count = item.inventory;
    let price = item.price;
    if (item.salePrice) {
        let count = item.saleInventory;
        if (count > 0) {
            price = item.salePrice;
        }
    }
    if (count) {
        return price;
    }
    return 0;
}

const item = {
  inventory: 3,
  price: 3,
  salePrice: 2,
  saleInventory: 0,
};
console.log(getLowestPrice(item));
