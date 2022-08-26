#include <iostream>
using namespace std;

void ConvertAndShow(const char *str) {
  auto f = atof(str);
  std::cout << f << '\n';
}


int main() {
  std::string number = "123.456";
  std::string_view svNum { number.data(), 3 };
  // ... some code
  std::string tempStr { svNum.data(), svNum.size() };
  ConvertAndShow(tempStr.c_str());
}
