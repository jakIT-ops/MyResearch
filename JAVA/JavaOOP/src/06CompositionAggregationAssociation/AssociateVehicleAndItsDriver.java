// Vehicle class
class Vehicle {

   String model;
   int id;

   Vehicle(String model, int id) { // Parameterized constructor
	    this.id = id;
      this.model = model;
   }

}

class Driver {

   String driverName;
   Vehicle vehicle;

   Driver(String name, Vehicle v) { // Parameterized constructor
	    vehicle = v;
	    this.driverName = name;
   }

}

class Main {

   public static void main(String args[]) {
      // Creating a Vehicle object with model: "Volvo S60", and id: "4453"
      Vehicle vehicle = new Vehicle("Volvo S60", 4453);
      // Creating a Driver object having name: "John" and passing the
      // vehicle in its constructor
	    Driver driver = new Driver("John", vehicle);
	    System.out.println(driver.driverName + " is a driver of car Id: " + driver.vehicle.id);
      // John is a driver of car Id: 4453
   }
}
