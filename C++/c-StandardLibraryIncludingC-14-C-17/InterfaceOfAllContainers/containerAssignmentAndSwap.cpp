// containerAssignmentAndSwap.cpp
#include <iostream>
#include <set>

int main(){
  std::set<int> set1{0, 1, 2, 3, 4, 5};
  std::set<int> set2{6, 7, 8, 9};

  for (auto s: set1) std::cout << s << " "; // 0 1 2 3 4 5
  std::cout << "\n";
  for (auto s: set2) std::cout << s << " "; // 6 7 8 9
  std::cout << "\n";

  set1= set2;
  for (auto s: set1) std::cout << s << " "; // 6 7 8 9
  std::cout << "\n";
  for (auto s: set2) std::cout << s << " "; // 6 7 8 9
  std::cout << "\n";

  set1= std::move(set2);//moves value of set2 in set1 and set2 becomes empty
  for (auto s: set1) std::cout << s << " "; // 6 7 8 9
  std::cout << "\n";
  for (auto s: set2) std::cout << s << " ";//prints null since set2 becomes empty after the move operation

  set2= {60, 70, 80, 90};
  for (auto s: set1) std::cout << s << " "; // 6 7 8 9
  std::cout << "\n";
  for (auto s: set2) std::cout << s << " "; // 60 70 80 90
  std::cout << "\n";

  std::swap(set1, set2);
  for (auto s: set1) std::cout << s << " "; // 60 70 80 90
  std::cout << "\n";
  for (auto s: set2) std::cout << s << " "; // 6 7 8 9
  std::cout << "\n";
  return 0;
}
