#include <iostream>
#include <vector>
#include <algorithm>

int main(){
  std::vector<int> myVec{1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
  std::for_each(myVec.begin(), myVec.end(), [](int& i){ 
    i= i*i; 
    std::cout << i << " "; 
  }); // 1 4 9 16 25 36 49 64 81 100

  return 0;
}
