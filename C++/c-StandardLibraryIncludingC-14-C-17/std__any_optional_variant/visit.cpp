// visit.cpp 
#include <iostream>
#include <variant>
#include <vector>

using namespace std;

int main(){
  std::vector<std::variant<char, long, float, int, double, long long>>      
           vecVariant = {5, '2', 5.4, 100ll, 2011l, 3.5f, 2017};

  for (auto& v: vecVariant){        
    std::visit([](auto&& arg){std::cout << arg << " ";}, v);    
                                   // 5 2 5.4 100 2011 3.5 2017                
  }
  cout<<std::endl;
  
  // display each type
  for (auto& v: vecVariant){
    std::visit([](auto&& arg){std::cout << typeid(arg).name() << " ";}, v);  
                                  // i c d x l f i (these letters refer to int char double __int64 long float int respectively
  }
  cout<<endl;
  
  // get the sum
  std::common_type<char, long, float, int, double, long long>::type res{};  
 
  std::cout << typeid(res).name() << std::endl;        // d (for double)
  
  for (auto& v: vecVariant){
    std::visit([&res](auto&& arg){res+= arg;}, v);     
  }
  std::cout << "res: " << res << std::endl;            // res: 4191.9
  
  // double each value
  for (auto& v: vecVariant){
    std::visit([](auto&& arg){arg *= 2;}, v);                           
    std::visit([](auto&& arg){std::cout << arg << " ";}, v);   
                                 // 10 d 10.8 200 4022 7 4034
  }
  return 0;
}
