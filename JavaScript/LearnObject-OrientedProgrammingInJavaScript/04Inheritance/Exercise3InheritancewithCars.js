// Base Class
class Vehicle {

    constructor(speed,model){
     var _speed = speed
     var _model = model
     this.getModel = function(){
       return _model
     }
     this.getSpeed = function(){
       return _speed
     }
    }  
  }
  
  // Derived Class
  class Car extends Vehicle {
    constructor(speed,model){
      super(speed,model)
      this.name = ""
    }
    
    // This function sets the name of the car
    setDetails(name) { // Setter Function
      this.name = name;
    }
  
    // This function calls the Base class functions and appends the result with the input 
    getDetails(carName) {
          var details = carName + ", " + this.getModel() + ", " + this.getSpeed(); // calling Base Class Function
          return details;
    }   
  }