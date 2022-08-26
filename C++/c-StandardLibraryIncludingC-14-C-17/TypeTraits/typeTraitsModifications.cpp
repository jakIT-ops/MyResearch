// typeTraitsModifications.cpp 
#include <iostream>
#include <type_traits>
using namespace std;

//output 0 if the function returns false and 1 if the function returns true
int main(){
  cout << is_const<int>::value << "\n";                     // 0
  cout << is_const<const int>::value << "\n";               // 1
  cout << is_const<add_const<int>::type>::value << "\n";    // 1

  typedef add_const<int>::type myConstInt;
  cout << is_const<myConstInt>::value << "\n";              //1

  typedef const int myConstInt2;
  cout << is_same<myConstInt, myConstInt2>::value << "\n";  // 1

  cout << is_same<int, remove_const<add_const<int>::type>::type>::value << "\n";    // 1
  cout << is_same<const int, add_const<int>::type>::value << "\n"; // 1
  
  return 0;
}
