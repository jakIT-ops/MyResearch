// performanceMeasurement.cpp 
#include <iostream>
#include <vector>
#include <chrono>
using namespace std;

int main(){
  std::vector<int> myBigVec(10000000, 2011);
  std::vector<int> myEmptyVec1;

  auto begin= std::chrono::high_resolution_clock::now();
  myEmptyVec1 = myBigVec;
  auto end= std::chrono::high_resolution_clock::now() - begin;

  auto timeInSeconds = std::chrono::duration<double>(end).count();
  std::cout << timeInSeconds << std::endl; // 0.0150688800 <- may vary from execution to execution

  return 0;
}
