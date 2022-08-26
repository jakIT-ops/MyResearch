// optional.cpp
#include <iostream>
#include <optional>
#include <vector>

std::optional<int> getFirst(const std::vector<int>& vec){
  if (!vec.empty()) return std::optional<int>(vec[0]);
  else return std::optional<int>();
}

int main(){
    
  std::vector<int> myVec{1, 2, 3};
  std::vector<int> myEmptyVec;
    
  auto myInt= getFirst(myVec);
    
  if (myInt){
    std::cout << *myInt << std::endl;                       // 1
    std::cout << myInt.value() << std::endl;                // 1
    std::cout << myInt.value_or(2017) << std::endl;         // 1
  }
    
  auto myEmptyInt= getFirst(myEmptyVec);
    
  if (!myEmptyInt){
    std::cout << myEmptyInt.value_or(2017) << std::endl;   // 2017
  }  
  
  return 0;
}
