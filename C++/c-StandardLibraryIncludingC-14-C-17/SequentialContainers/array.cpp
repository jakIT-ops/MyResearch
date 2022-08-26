// array.cpp 
#include <iostream>
#include <array>
#include <numeric>

using namespace std;

int main(){
  std::array<int, 10> arr{1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
  for (auto a: arr) std::cout << a << " " ;    // 1 2 3 4 5 6 7 8 9 10
  cout << "\n";

  double sum= accumulate(arr.begin(), arr.end(), 0);
  std::cout << sum << std::endl;               // 55

  double mean= sum / arr.size();
  std::cout << mean << std::endl;              // 5.5
  std::cout << (arr[0] == std::get<0>(arr));   // 1 (1 represents true)

  return 0;
}
