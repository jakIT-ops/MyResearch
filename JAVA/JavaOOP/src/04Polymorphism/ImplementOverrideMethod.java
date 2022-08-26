// Base Class
class Shape {

    // Private Data Members
    private double area;

    public Shape() { // Default Constructor
    	area = 0;
    }

    // Getter Function
    public double getArea() {
      return area;
    }

}

// Derived Class
class Circle extends Shape {

    private double radius;

    public Circle(double radius) { // Constructor
      this.radius = radius;
    }

    // Overridden Method the getArea() which returns the area of Circle

    public double getArea() {
      return (radius*radius) * 3.14;
    }

}

class Demo {

   public static void main(String args[]) {
       Shape circle = new Circle(2);
       System.out.println(circle.getArea());
       // out: 12.56
   }
}
