package main
import (
  "fmt"
)

func NextMutation(num []int) []int{
  /* Get the index of the second last number and compare it with the 
    number next to it, on the right. */
  index := len(num) - 2

  /* Find the index of the number num[index-1] which satisfies 
     the condition num[index] > num[index-1]. Here num[index] and num[index+1]
     represent two successive numbers in the sequence. */
  for index >= 0 && num[index] >= num[index + 1] {
    index--
  }

  /* Find the the number num[j] which is just larger than num[index-1]
   among the numbers lying to the right of num[index-1]. */
  if index >= 0 {
    j := len(num) - 1
    for num[j] <= num[index] {
      j--
    }
        
    // Swap num[index-1] and num[j]
    SwapNumbers(num, index, j);
  }

  /* Reverse the numbers following num[index-1], so that they are in 
     ascending order. */
  ReverseList(num, index + 1);

  return num;
}

// Reverse a list, given a starting index.
func ReverseList(num []int, start int) {
  i := start
  j := len(num) - 1

  for (i < j) {
    SwapNumbers(num, i, j)
    i++
    j--
  }
}

  // Swap numbers in a list, given their indexes. 
func SwapNumbers(num []int, i int, j int) {
  temp := num[i]
  num[i] = num[j]
  num[j] = temp
}

func main() {
  // Driver code
  num := []int{4,5,2,6,7,3,1}
  fmt.Println("Input:",num)
  
  result := NextMutation(num)
  fmt.Println("Output:",result)
}
