function Shape(name,sides){
    this.name = name
    this.sides = sides
  }
  
  Shape.prototype.displayName = function(){
    return this.name
  }
  
  function Triangle(name,sides,a,b,c){
   
    Shape.call(this,name,sides)
    this.a = a
    this.b = b
    this.c = c
  }
  
  Triangle.prototype = Object.create(Shape.prototype)
  
  Triangle.prototype.constructor = Triangle
  
  
  Triangle.prototype.triangleType = function(){
    if((this.a == this.b && this.b == this.c)){
      return "Equilateral"
    }
    else if(this.a == this.b|| this.a == this.c|| this.b == this.c){
      return "Isosceles"
    }else{
      return "Scalene"
    }
  }