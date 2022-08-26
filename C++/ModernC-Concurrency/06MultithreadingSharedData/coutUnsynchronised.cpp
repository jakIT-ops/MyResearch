// coutUnsynchronised.cpp

#include <chrono>
#include <iostream>
#include <thread>

class Worker{
public:
  Worker(std::string n):name(n){};
    void operator() (){
      for (int i = 1; i <= 3; ++i){
        // begin work
        std::this_thread::sleep_for(std::chrono::milliseconds(200));
        // end work
        std::cout << name << ": " << "Work " << i << " done !!!" << std::endl;
      }
    }
private:
  std::string name;
};


int main(){

  std::cout << std::endl;
  
  std::cout << "Boss: Let's start working.\n\n";
 
  std::thread herb= std::thread(Worker("Herb"));
  std::thread andrei= std::thread(Worker("  Andrei"));
  std::thread scott= std::thread(Worker("    Scott"));
  std::thread bjarne= std::thread(Worker("      Bjarne"));
  std::thread bart= std::thread(Worker("        Bart"));
  std::thread jenne= std::thread(Worker("          Jenne"));
  
  
  herb.join();
  andrei.join();
  scott.join();
  bjarne.join();
  bart.join();
  jenne.join();
  
  std::cout << "\n" << "Boss: Let's go home." << std::endl;
  
  std::cout << std::endl;
  
}

/*
 *Boss: Let's start working.

          Jenne: Work 1 done !!!
        Bart: Work 1 done !!!
  Andrei: Work 1 done !!!
      Bjarne: Work 1 done !!!
    Scott: Work 1 done !!!
Herb: Work 1 done !!!
          Jenne: Work 2 done !!!
    Scott: Work 2 done !!!
        Bart  Andrei: Work 2 done !!!
: Work 2 done !!!
      Bjarne: Work 2 done !!!
Herb: Work 2 done !!!
          Jenne    Scott  Andrei: : : Work Work Work 333 done !!! done !!! done !!!


        Bart: Work 3 done !!!
      Bjarne: Work 3 done !!!
Herb: Work 3 done !!!

Boss: Let's go home.

 * **/
