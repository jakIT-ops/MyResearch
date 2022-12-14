#include <iostream>
using namespace std;

template<typename T> void linePrinter(const T& x)
{
  if constexpr (std::is_integral_v<T>){
    std::cout << "num: " << x << '\n';
  }
  else if constexpr (std::is_floating_point_v<T>){
    const auto frac = x - static_cast<long>(x);
    std::cout << "flt: " << x << ", frac " << frac << '\n';
  }
  else if constexpr(std::is_pointer_v<T>){
    std::cout << "ptr, ";
    linePrinter(*x);
  }
  else{
    std::cout << x << '\n';
  }
}

template<typename ... Args>
void PrintWithInfo(Args ... args)
{
  (linePrinter(std::forward<Args>(args)), ...); // fold expression over the comma operator
}

int main(){
  std::cout << "-- extra info: \n";
  int i = 10;
  PrintWithInfo(&i, std::string("hello"), 10, 20.5, 30);
}
