package main
import (
  "fmt"
  "strings"
)

func InOrderBST(array []string, n int) bool {
  if n == 0 || n == 1 { // Return true if array has one or no element
    return true;
  }
    for i := 1; i < n; i++ { // Found the unsorted pair
    if strings.Compare(array[i - 1], array[i]) == 1 {
      return false
    }
  }
  return true // No unsorted pair found
}

func main(){
  // Driver code
  array := []string{ "Caryl", "Elia", "Elvira", "Jeanette", "Lala", "Latasha", "Lyn"}
  n := len(array)
  if InOrderBST(array, n) {
      fmt.Println("Valid BST")
  } else {
      fmt.Println("Not valid BST")
  }
}
