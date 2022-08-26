package main
import "fmt"

func goalsFulfilled(trades []int) bool {
    frequencyMap := make(map[int]int)
    imaginedMap := make(map[int]int)

    for _, n := range trades {
        frequencyMap[n] = 1
    } 

    for _ , n := range trades {
        if frequencyMap[n] == 0 {
            continue
        } else if i, ok := imaginedMap[n]; ok && i > 0 {
            // Adding number to existing sequence
            imaginedMap[n] = i - 1
            if j, ok := imaginedMap[n + 1]; ok {
                imaginedMap[n + 1] = j + 1
            } else {
                imaginedMap[n + 1] = 1
            }
            
        } else if frequencyMap[n+1] > 0 && frequencyMap[n+2] > 0 {
          // Creating new subsequence
          frequencyMap[n+1] = frequencyMap[n+1] - 1
          frequencyMap[n+2] = frequencyMap[n+2] - 1
          imaginedMap[n+3] = imaginedMap[n+3] + 1
        } else {
            return false
        }
        if val, ok := frequencyMap[n]; ok {
            frequencyMap[n] = val - 1
        } else {
            frequencyMap[n] = -1
        }
    }
    return true
}


func main() {
    // Driver code

    trades := []int{1, 2, 3, 3, 4, 4, 5, 5}
    
    if !goalsFulfilled(trades) {
      fmt.Println("The goals have not been fulfilled!")
    } else{
      fmt.Println("The goals have been fulfilled!")
    }
}
