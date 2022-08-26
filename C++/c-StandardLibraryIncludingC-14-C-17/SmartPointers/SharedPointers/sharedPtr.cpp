// sharedPtr.cpp 
#include <iostream>
#include <memory>

class MyInt{
public:
  MyInt(int v):val(v){
    std::cout << "Hello: " << val << std::endl;
  }
  ~MyInt(){
    std::cout << "Good Bye: " << val << std::endl;
  }
private:
  int val;
};

int main(){
  auto sharPtr= std::make_shared<MyInt>(1998);        // Hello: 1998
  std::cout << sharPtr.use_count() << std::endl;      // 1

  {
    std::shared_ptr<MyInt> locSharPtr(sharPtr);
    std::cout << locSharPtr.use_count() << std::endl; // 2
  }
  std::cout << sharPtr.use_count() << std::endl;      // 1

  std::shared_ptr<MyInt> globSharPtr= sharPtr;
  std::cout << sharPtr.use_count() << std::endl;      // 2

  globSharPtr.reset();
  std::cout << sharPtr.use_count() << std::endl;     // 1
  sharPtr= std::shared_ptr<MyInt>(new MyInt(2011));  // Hello:2011                                                   // Good Bye: 1998
  // Good Bye: 1998
  // Good Bye: 2011
  return 0;
}

