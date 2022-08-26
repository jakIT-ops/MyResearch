function getBill(item) {
    return {
        name: item.name,
        due: twoWeeksFromNow(),
        total: calculateTotal(item.price),
    };
}


const bill = getBill({ name: 'Room Cleaning', price: 30 });

function displayBill(bill) {
    return `Your total is ${bill.total} for ${bill.name} is due on ${bill.due}`;
}

console.log("Displaying the bill: " + displayBill(bill));
