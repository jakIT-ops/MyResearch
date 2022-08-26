package main
import (
  "fmt"
  "math"
)

func SimilarityExtent(Sample1 string, Sample2 string) int{
  n := len(Sample1)
  m := len(Sample2)

  // Initialize an array to store all the computations
  D := make([][]int, n + 1)

  /* Cater the base case of the edit distance between 
     an empty string and non-empty string. */
  for i := 0; i <= n; i++ {
    D[i] = make([]int, m + 1)
    D[i][0] = i;
  }

  for j := 0; j <= m; j++ {
    D[0][j] = j;
  }

  /* Loop over the nucleotides both samples and compute the 
     edit distances D[i][j]'s. */
  for i := 1; i <= n; i++ {
    for j := 1; j <= m; j++ {

      Up := D[i - 1][j];
      Left := D[i][j - 1];
      UpLeft := D[i - 1][j - 1];

      if Sample1[i - 1] == Sample2[j - 1] {
        D[i][j] = 1 + int(math.Min(float64(Up), math.Min(float64(Left), float64(UpLeft - 1))))
      }else if Sample1[i - 1] != Sample2[j - 1] {
        D[i][j] = 1 + int(math.Min(float64(Up), math.Min(float64(Left), float64(UpLeft))))
      }
    }
  }
  return D[n][m]
}

//Driver code
func main(){
  Sample1 := "abcdef";
  Sample2 := "azced";

  operations := SimilarityExtent(Sample1, Sample2);

  fmt.Println(operations);
}
