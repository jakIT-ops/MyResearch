class Solution {
  static void insert(int[] array, int rightIndex, int value) {
    int j = rightIndex;
    for(;
        j >= 0 && array[j] > value;
        j--) {
      array[j + 1] = array[j];
    }   
    array[j + 1] = value; 
  }

  public static void insertionSort(int[] array) {
    //Write this method
    
    return;
  }
}
