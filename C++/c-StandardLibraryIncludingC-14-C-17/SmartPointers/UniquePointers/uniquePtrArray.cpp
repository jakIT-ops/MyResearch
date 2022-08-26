// uniquePtrArray.cpp 
#include <iostream>
#include <memory>

using namespace std;

class MyStruct{
public:
  MyStruct():val(count){
    cout << static_cast<void*>(this) << " Hello: " << val << endl;
    MyStruct::count++;
  }
  ~MyStruct(){
    cout << static_cast<void*>(this) << " Good Bye: " << val << endl;
    MyStruct::count--;
  }
private:
  int val;
  static int count;
};

int MyStruct::count= 0;

int main(){
  {
    // generates a myUniqueArray with thre `MyStructs` 
    unique_ptr<MyStruct[]> myUniqueArray{new MyStruct[3]};
  }
  // 0x1200018 Hello: 0
  // 0x120001c Hello: 1
  // 0x1200020 Hello: 2
  // 0x1200020 GoodBye: 2
  // 0x120001c GoodBye: 1
  // 0x1200018 GoodBye: 0

  return 0;
}
