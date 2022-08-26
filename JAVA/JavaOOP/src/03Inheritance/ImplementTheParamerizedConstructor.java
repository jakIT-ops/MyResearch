// Base Class
class Laptop {

  // Private Data Members
  private String name;

  public Laptop() { // Default Constructor
    name = "";
  }

  public Laptop(String name) { // Default Constructor
    this.name = name;
  }

  // Getter Function
  public String getName() {
    return name;
  }

}

// Derived Class
class Dell extends Laptop {

  public Dell() { // Default Constructor

  }

  public Dell(String name) { // Parametrized Constructor
   super(name);
  }

  public String getDetails() {
    return getName();
  }

  public static void main(String args[]) {
     Dell dell = new Dell("Dell Inspiron");
     System.out.println(dell.getDetails());
  }

}
