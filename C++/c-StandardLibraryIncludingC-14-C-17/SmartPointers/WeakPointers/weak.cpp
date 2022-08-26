#include <iostream>
#include <memory>

int main(){
  auto sharedPtr= std::make_shared<int>(2011);
  std::weak_ptr<int> weakPtr(sharedPtr);

  std::cout << weakPtr.use_count() << std::endl;       // 1
  std::cout << sharedPtr.use_count() << std::endl;     // 1

  std::cout << weakPtr.expired() << std::endl;         // false
  if( std::shared_ptr<int> sharedPtr1= weakPtr.lock() ) {
    std::cout << *sharedPtr << std::endl; // 2011
  }
  else{
    std::cout << "Don't get it!" << std::endl;
  }

  weakPtr.reset();

  if( std::shared_ptr<int> sharedPtr1= weakPtr.lock() ) {
    std::cout << *sharedPtr << std::endl;
  }
  else{
    std::cout << "Don't get it!" << std::endl;         // Don't get it!
  }
  
  return 0;
}
