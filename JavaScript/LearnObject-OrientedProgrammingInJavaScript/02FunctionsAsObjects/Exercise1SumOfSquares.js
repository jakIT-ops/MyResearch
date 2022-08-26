function SquareSum(num1,num2,num3){
    this.num1 = num1
    this.num2 = num2
    this.num3 = num3
    this.squaresum = function(){
      this.num1 = this.num1*this.num1
      this.num2 = this.num2*this.num2
      this.num3 = this.num3*this.num3
      this.answer = this.num1+this.num2+this.num3
      return this.answer
    }
}