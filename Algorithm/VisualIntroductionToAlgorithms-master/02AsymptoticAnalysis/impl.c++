int linearSearch(const vector<int>& array,
                 const int targetValue) {
  for (int guess = 0; guess < array.size(); guess++) {
    if (array[guess] == targetValue) { 
        return guess;  // found it!
    }
  }
  
  return -1;  // didn't find it
}
