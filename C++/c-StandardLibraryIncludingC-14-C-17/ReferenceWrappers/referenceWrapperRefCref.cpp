// referenceWrapperRefCref.cpp 
#include <iostream>
#include <functional>

void invokeMe(const std::string& s){
  std::cout << s << ": const " << std::endl;
}

template <typename T>
  void doubleMe(T t){ 
  t*= 2; 
}

int main(){
  std::string s{"string"};

  invokeMe(std::cref(s));        // string
  
  int i= 1;
  std::cout << i << std::endl;   // 1

  doubleMe(i);
  std::cout << i << std::endl;   // 1S

  doubleMe(std::ref(i));
  std::cout << i << std::endl;   // 2
  
  return 0;
}
