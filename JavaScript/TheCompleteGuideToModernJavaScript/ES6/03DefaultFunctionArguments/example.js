function calculatePrice(total, tax = 0.1, tip = 0.05){
  console.log(total + (total * tax) + (total * tip));
}
// The 0.15 will be bound to the second argument, tax even if in our intention it was to set 0.15 as the tip
calculatePrice(100, 0.15)
