#include <vector>
using namespace std;

void insert(vector<int>& array, int rightIndex, int value) {
  int j = rightIndex;
  for(;
      j >= 0 && array[j] > value;
      j--) {
    array[j + 1] = array[j];
  }   
  array[j + 1] = value; 
}

void insertionSort(vector<int>& array) {
  // Write this method		
  return;
}
