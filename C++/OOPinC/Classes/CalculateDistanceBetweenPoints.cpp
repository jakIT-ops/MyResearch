#include <iostream>
#include <cmath>
using namespace std;

class Point {

  // Private fields
  private:
  int x;
  int y;

  public:

  // Default Constructor
  Point() {
    x = 0;
    y = 0;
  }

  // Parameterized Constructor
  Point(int x, int y) { 
    this->x = x;
    this->y = y;
  }


  double distance() {
    double distance = sqrt(x*x + y*y);
    return distance;
  }

  double distance(int x2, int y2) {
    double distance = sqrt(((x2-x)*(x2-x))+((y2-y)*(y2-y)));
    return distance;
  }

};
