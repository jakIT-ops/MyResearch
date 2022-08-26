function Calculator(num1,num2) {
  
    this.num1 = num1
    this.num2 = num2
 
   // Addition Method
   this.add = function() {
     return this.num1 + this.num2
   }
 
   // Subtraction Method
   this.subtract = function() {
     return this.num2 - this.num1
   }
   // Multiplication Method
   this.multiply = function() {
     return this.num1 * this.num2;
   }
 
    // Divison Method
   this.divide = function() {
     return this.num2 / this.num1;
   }
 }