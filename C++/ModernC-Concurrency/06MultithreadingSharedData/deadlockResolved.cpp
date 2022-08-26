// deadlockResolved.cpp

#include <iostream>
#include <chrono>
#include <mutex>
#include <thread>

using namespace std;

struct CriticalData{
  mutex mut;
};

void deadLock(CriticalData& a, CriticalData& b){

  lock_guard<std::mutex> guard1(a.mut, std::adopt_lock);
  cout << "Thread: " << this_thread::get_id() << " first mutex" << endl;

  this_thread::sleep_for(chrono::milliseconds(1));

  lock_guard<std::mutex> guard2(b.mut, std::adopt_lock);
  cout << "  Thread: " << this_thread::get_id() << " second mutex" <<  endl;

  cout << "    Thread: " << this_thread::get_id() << " get both mutex" << endl;
  lock(a.mut, b.mut);
  // do something with a and b
}

int main(){

  cout << endl;

  CriticalData c1;
  CriticalData c2;

  thread t1([&]{deadLock(c1,c2);});
  thread t2([&]{deadLock(c2,c1);});

  t1.join();
  t2.join();

  cout << endl;

}
