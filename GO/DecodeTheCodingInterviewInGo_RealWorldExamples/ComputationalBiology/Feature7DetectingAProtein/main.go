package main
import (
  "fmt"
)

func IsProtein(s string) bool{
  // Create a hashmap to keep track of the nucleotides and their occurences
  HashMap := make(map[byte]int)

  // Traverse the sequence and create a new entry for every new nucleotide found.
  // If a nucleotide, that is already in the hashmap, is found, get its current 
  // occurence and increment 1 to it. 
  for i := 0; i < len(s); i++ {
    if _, ok := HashMap[s[i]]; !ok{
      HashMap[s[i]] = 0
    }
    occurence := HashMap[s[i]] + 1;
    HashMap[s[i]] = occurence
  }

  count := 0

  // Traverse the hashmap and update the count by 1, whenever a 
  // nucleotide with odd number of occurences is found.
  for _, value := range HashMap {
    count += value % 2
  }
  if (count <= 1) {
    return true;
  } else {
    return false;
  }
}

//Driver code
func main(){
  sequence := "baefeab"
  isProtein := IsProtein(sequence)
  fmt.Println("Input:", sequence)
  fmt.Println("Output:", isProtein, "\n")

  sequence = "abc"
  isProtein = IsProtein(sequence)
  fmt.Println("Input: ", sequence)
  fmt.Println("Output: ", isProtein)
}
