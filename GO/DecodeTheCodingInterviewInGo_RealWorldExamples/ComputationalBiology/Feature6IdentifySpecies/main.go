package main
import (
  "fmt"
)

func FindSpeciesMarker(Nucleotide string) string{
    
  // Check if a DNA sequence has no Nucleotide
  if len(Nucleotide) == 0 {
    return "DNA sequence must have atleast one Nucleotide."
  } 

  n := len(Nucleotide)
  stCurr, longest, currLen, start, i := 0, 0, 0, 0, 0

  Window := make(map[byte]int)

  // Traverse the DNA sequence to find the longest substring 
  // without repeating characters. 
  for i = 0; i < n; i++ {
      // If the current Nucleotide is not present in the hash map,
      // then store it in the hash map with the value as the current index.
    if _, ok := Window[Nucleotide[i]]; !ok {
      Window[Nucleotide[i]] = i
    } else {
      // If the current Nucleotide is present in the hash map, 
      // it means that this Nucleotide can be repeated. 
      // Check if the current Nucleotide occurs before or after `stCurr`. 
      if Window[Nucleotide[i]] >= stCurr {
        currLen = i - stCurr
        if longest < currLen {
          longest = currLen
          start = stCurr
        }
        // The next substring will start after the last 
        // occurence of the current Nucleotide. 
        stCurr = Window[Nucleotide[i]] + 1
      }
      // Update the last occurence of 
      // the Nucleotide in the hash map
      Window[Nucleotide[i]] = i
      }
    }
    // Update the longest substring's 
    // length and starting index.
    if (longest < i - stCurr){
      longest = i - stCurr;
      start = stCurr;
    }
  return Nucleotide[start:start + longest]
}

//Driver code
func main() {
  Nucleotide := "abcdbea";
  str := FindSpeciesMarker(Nucleotide);
  fmt.Println("Specie marker:", str);
  fmt.Println("Length of specie marker:", len(str));
}
