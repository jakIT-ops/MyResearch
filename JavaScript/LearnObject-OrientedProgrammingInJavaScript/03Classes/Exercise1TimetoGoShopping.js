class Product{  
    constructor(_name,_price,_amount,_madeIn){
      var _name = _name
      var _price = _price
      var _amount = _amount
      var _madeIn = _madeIn
      
      this.getName = function(){
        return _name
      }
      this.getPrice = function(){
        return _price
      }
      this.getAmount = function(){
        return _amount
      }
      this.setAmount = function(num){
        _amount = num
      }
      this.getMadeIn = function(){
        return _madeIn
      }
    }
    canSell(num){
      if(this.getAmount() < num){
        return false
      }else{
        return true
      }
    }
    sell(num){
      var temp = this.getAmount()
      if(this.canSell(num)){
        this.setAmount(temp-num) 
        return this.getAmount()
      }else{
        this.setAmount(temp + (num*2)) 
        return this.getAmount()
      }
    }
  
  }