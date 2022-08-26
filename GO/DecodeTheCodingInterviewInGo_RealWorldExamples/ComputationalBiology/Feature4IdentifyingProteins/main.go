package main
import (
    "fmt"
)

func isProtein(sequence string) bool{
    if len(sequence) <= 1 {
        return true
    } else {
        if sequence[0] == sequence[len(sequence)-1] {
            return isProtein(sequence[1: len(sequence) - 1])
        }
    }
    return false
}

func main() {
    // Driver code
    
    protein := "acbca"
    fmt.Printf("Is %v a Protein? = %v\n", protein, isProtein(protein))
}
