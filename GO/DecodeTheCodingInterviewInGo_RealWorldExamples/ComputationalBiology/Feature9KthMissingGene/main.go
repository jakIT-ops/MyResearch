package main
import (
  "fmt"
)

func FindKthMissingGene(A []int, k int) int {
  Left := 0
  Right := len(A) - 1;

  for Left <= Right {
    // We choose the Pivot, which is the middle index of the array, A.
    Pivot := (Left + Right) / 2;

  /* If the number of missing genes before the current gene 
     is less than k, we will continue to search on the Right side of A. */
    if A[Pivot] - Pivot - 1 < k {
      Left = Pivot + 1;
    }else { // // Otherwise, we will continue to search on the Left of A.
      Right = Pivot - 1;
    }
  }
  return Left + k;
}

//Driver code
func main(){
    A := []int{2,3,4,7,11}
    k := 5

    MissingGenes := FindKthMissingGene(A, k);

    fmt.Println("The kth missing gene is:", MissingGenes);
  }
