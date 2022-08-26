// Base Class
class Shape {

  // Private Data Members
  private String name;

  public Shape() { // Default Constructor
  	name = "Shape";
  }

  // Getter Function
  public String getName() {
    return name;
  }

}

// Derived Class
class XShape extends Shape {

  private String name;

  public XShape(String name) { // Default Constructor
    this.name = name;
  }

  // Overridden Method
  public String getName() {
    return super.getName() + ", " + this.name;
  }

}

class Demo {

    public static void main(String args[]) {
       Shape circle = new XShape("Circle");
       System.out.println(circle.getName());
       // Out: Shape, Circle
    }
}
