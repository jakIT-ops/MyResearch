#include <iostream>
#include <queue>

int main(){
  std::queue<int> myQueue;

  std::cout << myQueue.empty() << std::endl;    // true
  std::cout << myQueue.size() << std::endl;     // 0

  myQueue.push(1);
  myQueue.push(2);
  myQueue.push(3);
  std::cout << myQueue.back() << std::endl;     // 3
  std::cout << myQueue.front() << std::endl;    // 1

  while (!myQueue.empty()){
    std::cout << myQueue.back() << " ";
    std::cout << myQueue.front() << " : ";
    myQueue.pop();
  }                                             // 3 1 : 3 2 : 3 3

  std::cout << std::endl << myQueue.empty() << std::endl;    //1 (denotes true)
  std::cout << myQueue.size() << std::endl;     // 0

  return 0;
}
