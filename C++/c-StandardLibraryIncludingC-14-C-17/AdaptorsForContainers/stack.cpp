// stack.cpp
#include <iostream>
#include <stack>

int main(){

  std::stack<int> myStack;

  std::cout << myStack.empty() << std::endl;   // true
  std::cout << myStack.size() << std::endl;    // 0

  myStack.push(1);
  myStack.push(2);
  myStack.push(3);
  std::cout << myStack.top() << std::endl;     // 3

  while (!myStack.empty()){ 
    std::cout << myStack.top() << " ";
    myStack.pop();
  }                                            // 3 2 1

  std::cout << std::endl << myStack.empty() << std::endl;   // 1 (denotes true)
  std::cout << myStack.size() << std::endl;    // 0

  return 0;
}
