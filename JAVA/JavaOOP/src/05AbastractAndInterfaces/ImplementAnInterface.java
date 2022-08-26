// Addition interface
interface Addition {

  int add(int num1, int num2);

}

// Calculator Class Implementing the Addition Interface
class Calculator implements Addition {

  // Overriding the add method of Addition interface
  public int add(int num1, int num2) {
    return num1 + num2;
  }

}

class Demo {

   public static void main(String args[]) {
     Calculator cal = new Calculator();
     System.out.println(cal.add(10, 20));
     // 30
   }
}
