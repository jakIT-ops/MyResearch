// Base Class
class Vehicle {

  // Private Data Members
  private String speed;
  private String model;

  public Vehicle() { // Default Constructor
    speed = "100";
    model = "Tesla";
  }

  // Getter Function
  public String getSpeed() {
    return speed;
  }

  // Getter Function
  public String getModel() {
    return model;
  }

}

// Derived Class
class Car extends Vehicle {

  public String name; //  Name of a Car

  public Car() { // Default Constructor
    name = "";
  }

  // This function sets the name of the car
  public void setDetails(String name) { // Setter Function
    this.name = name;
  }

  // This function calls the Base class functions and append the result with input
  public String getDetails(String carName) {
    String details = carName + ", " + getModel() + ", " + getSpeed(); // calling Base Class Function
    return details;
  }

  public static void main(String args[]) {
    Car car = new Car();
    System.out.println(car.getDetails("X"));
  }

}
