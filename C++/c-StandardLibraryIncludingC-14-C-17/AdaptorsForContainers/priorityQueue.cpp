// priorityQueue.cpp 
#include <iostream>
#include <queue>

int main(){
  std::priority_queue<int> myPriorityQueue;

  std::cout << "is empty:\t" << myPriorityQueue.empty() << std::endl;   // 1 (denotes true)
  std::cout << "size:\t\t" << myPriorityQueue.size() << std::endl;    // 0

  myPriorityQueue.push(3);
  myPriorityQueue.push(1);
  myPriorityQueue.push(2);
  std::cout << "top:\t\t" << myPriorityQueue.top() << std::endl;     // 3

  std::cout<< "Data:\t";
  while (!myPriorityQueue.empty()){
    std::cout << myPriorityQueue.top() << " ";
    myPriorityQueue.pop();
  }                                                    // 3 2 1
  std::cout << std::endl;

  std::cout << "is empty:\t" << myPriorityQueue.empty() << std::endl;   // 1 (denotes true)
  std::cout << "size:\t\t" << myPriorityQueue.size() << std::endl;    // 0

  std::priority_queue<std::string, std::vector<std::string>,
                    std::greater<std::string>> myPriorityQueue2;

  myPriorityQueue2.push("Only");
  myPriorityQueue2.push("for");
  myPriorityQueue2.push("testing");
  myPriorityQueue2.push("purpose");
  myPriorityQueue2.push(".");

  while (!myPriorityQueue2.empty()){
    std::cout << myPriorityQueue2.top() << " ";
    myPriorityQueue2.pop();
  }                                // . Only for purpose testing
  return 0;
}
