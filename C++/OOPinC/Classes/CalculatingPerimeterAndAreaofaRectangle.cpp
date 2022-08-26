class Rectangle {

   public:
   float length, height;
   Rectangle(float l, float h) {
     length = l;
     height = h;
   }
  
   float perimeter() { 
    return length*2  + height*2;
   }

   float area() { 
    return length*height;
   }
};
