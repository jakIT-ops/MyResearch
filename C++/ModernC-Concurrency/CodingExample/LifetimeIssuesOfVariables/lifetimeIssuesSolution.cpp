// lifetimeIssuesSolution.cpp

#include <iostream>
#include <string>
#include <thread>

int main(){
    
  std::cout << "Begin:" << std::endl;               

  std::string mess{"Child thread"};

  std::thread t([&mess]{ std::cout << mess << std::endl;});
  t.join();                                   
  
  std::cout << "End:" << std::endl;             

}

/*
 *Begin:
Child thread
End:
 * */
