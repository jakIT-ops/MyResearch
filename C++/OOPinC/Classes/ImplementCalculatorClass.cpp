class calculator{
  float num1, num2;
  public:
  calculator() {
    num1 = 0;
  	num2 = 0;
  }

  int add(float n1, float n2){
    num1 = n1;
    num2 = n2;
    return num1 + num2;
  }

  float subtract(float n1, float n2){
    num1 = n1;
    num2 = n2;
    return num2 - num1;
  }

  float multiply(float n1, float n2){
    num1 = n1;
    num2 = n2;
    return num1 * num2;
  }

  float divide(float n1, float n2){
    num1 = n1;
    num2 = n2;
    return num2 / num1;
  }
};
