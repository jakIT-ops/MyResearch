// duration.cpp 
#include <iostream>
#include <chrono>
#include <ratio>
using namespace std;
using namespace std::chrono;
template <class Rep, class Period = ratio<1>> class duration;

int main(){
  typedef std::chrono::duration<long long, std::ratio<1>> MySecondTick;
  MySecondTick aSecond(1);

  milliseconds milli(aSecond);
  std::cout << milli.count() << " ms\n";        // 1000 milli

  seconds seconds(aSecond);
  std::cout << seconds.count() << " sec\n";         // 1 sec

  minutes minutes(duration_cast<minutes>(aSecond));
  std::cout << minutes.count() << " min\n";         // 0 min

  typedef std::chrono::duration<double, std::ratio<2700>> MyLessonTick;
  MyLessonTick myLesson(aSecond);
  std::cout << myLesson.count() << " less\n";       // 0.00037037 less

  return 0;
}
