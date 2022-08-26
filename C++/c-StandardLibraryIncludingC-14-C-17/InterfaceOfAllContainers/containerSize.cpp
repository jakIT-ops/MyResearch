// containerSize.cpp 
#include <iostream>
#include <map>
#include <set>
#include <vector>

using namespace std;

int main(){
  vector<int> intVec{1, 2, 3, 4, 5, 6, 7, 8, 9};
  map<string, int> str2Int = {{"bart", 12345}, 
                            {"jenne", 34929}, {"huber", 840284}};
  set<double> douSet{3.14, 2.5};

  cout << intVec.empty() << endl;  // false
  cout << str2Int.empty() << endl; // false
  cout << douSet.empty() << endl;  // false

  cout << intVec.size() << endl;  // 9
  cout << str2Int.size() << endl; // 3
  cout << douSet.size() << endl;  // 2

  cout << intVec.max_size() << endl;  // 4611686018427387903
  cout << str2Int.max_size() << endl; // 384307168202282325
  cout << douSet.max_size() << endl;  // 461168601842738790
  return 0;
}
