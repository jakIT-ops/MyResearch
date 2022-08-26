package main
import (
    "fmt"
    "math"
)

func detectVirus(s string, k int) string{
    if len(s) * k == 0 {
        return ""
    } 

    // left and right pointers
    left, right := 0, 0

    // dummy variables
    start, end := 0, 0

    // character -> its rightmost position
    characterMap := make(map[byte]int)

    for right < len(s) {
        // add new character and move right pointer
        characterMap[s[right]] = right
        right++
        // This clause checks if window contains more than k characters
        if len(characterMap) == k + 1 {
                minIdx := math.MaxInt64
                for _, val := range characterMap {
                    if val < minIdx {
                        minIdx = val
                    }
                }
                delete(characterMap, s[minIdx])
                // move left pointer of the window
                left = minIdx + 1
        }

        if end - start < right - left{
            start = left
            end = right
        }
        
    }
    return s[start: end]
}


func main() {
    // Driver code
    infectedDNA := "ababffzzeee"
    k := 3// Supplied from a hidden program
    
    fmt.Println(detectVirus(infectedDNA, k))
}
