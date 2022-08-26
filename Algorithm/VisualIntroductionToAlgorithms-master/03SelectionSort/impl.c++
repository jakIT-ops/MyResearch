#include <vector>
using namespace std;

void swap(vector<int> array, int firstIndex, int secondIndex) {
    int temp = array[firstIndex];
    array[firstIndex] = array[secondIndex];
    array[secondIndex] = temp;
}

int indexOfMinimum(vector<int> array, int startIndex) {
    int minValue = array[startIndex];
    int minIndex = startIndex;

    for(int i = minIndex + 1; i < array.size(); i++) {
        if(array[i] < minValue) {
            minIndex = i;
            minValue = array[i];
        }
    } 
    return minIndex;
}; 

void selectionSort(vector<int>& array) {
  // Write this method
  
};
