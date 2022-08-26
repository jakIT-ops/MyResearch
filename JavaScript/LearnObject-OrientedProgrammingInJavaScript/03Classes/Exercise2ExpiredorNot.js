class Product{  
    constructor(name,price,amount,madeIn,expiryDate,brand){
      //initializing properties 
      this.name = name
      this.price = price
      this.amount = amount
      this.madeIn = madeIn
      this.expiryDate = expiryDate 
      this.brand = brand
    }
     //it compares expiry dates of two students
    static checkExpiry(product1, product2){
      //getting the current date
      var currentDate = new Date()
      //first case: both the products have already expired
      if((product1.expiryDate < currentDate) && (product2.expiryDate < currentDate)){
        return "Neither"
      }
      //second case: product1 has expired but product2 has not
      else if((product1.expiryDate < currentDate) && (product2.expiryDate > currentDate)){
        return product2.brand
      }
      //third case: product2 has expired but product1 has not
      else if((product1.expiryDate > currentDate) && (product2.expiryDate < currentDate)){
        return product1.brand
      }
      //fourth case: neither of the products have expired
      else if ((product1.expiryDate > currentDate) && (product2.expiryDate > currentDate)) {
        //returning product1's brand name if its expiry date is later than product2's
        if((product1.expiryDate - currentDate) > (product2.expiryDate - currentDate)){
          return product1.brand
        }
        //returning product2's brand name if its expiry date is later than product1's
        else if((product1.expiryDate - currentDate) < (product2.expiryDate - currentDate)){
          return product2.brand
        }
        //returning "Either"  if both the products expire on same date in future
        else{
          return "Either"
        }
      }
    }
  }