#include <iostream>
#include <functional>

// for placehoder _1 and _2
using namespace std::placeholders; 

using std::bind;
using std::function;

double divMe(double a, double b){ return a/b; };

int main(){
  function < double(double, double) > myDiv1= bind(divMe, _1, _2);
  function < double(double) > myDiv2= bind(divMe, 2000, _1);
  std::cout << (divMe(2000, 10) == myDiv1(2000, 10) == myDiv2(10)); // 0
}
