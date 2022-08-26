#include <iostream>
using namespace std;

// A simple Shape interface which provides a method to get the Shape's area
class Shape {
  public:
  float getArea(){}
};

// A Rectangle is a Shape with a specific width and height
class Rectangle : public Shape {   // derived form Shape class
  private:
  float width;
  float height;

  public:
  Rectangle(float wid, float heigh) {
    width = wid;
    height = heigh;
  }
  float getArea(){
    return width * height; 
  }
};

// A Circle is a Shape with a specific radius
class Circle : public Shape {
  private:
  float radius;

  public:
  Circle(float rad){
    radius = rad; 
  }
  float getArea(){
    return 3.14159f * radius * radius; 
  }
};

int main() {
  Rectangle r(2, 6);    // Creating Rectangle object

  Shape* shape = &r;   // Referencing Shape class to Rectangle object

  cout << "Calling Rectangle getArea function: " << r.getArea() << endl;      // Calls Rectangle.printArea()
  cout << "Calling Rectangle from shape pointer: " <<  shape->getArea() << endl <<endl; // Calls shape's dynamic-type's
  
  Circle c(5);    // Creating Circle object

  shape = &c;   // Referencing Shape class to Circle object
  
  cout << "Calling Circle getArea function: " << c.getArea() << endl;
  cout << "Calling Circle from shape pointer: " <<shape->getArea() << endl << endl; 
}

/**
 *Calling Rectangle getArea function: 12
Calling Rectangle from shape pointer: 0

Calling Circle getArea function: 78.5397
Calling Circle from shape pointer: 2.34181e-38
 * */
