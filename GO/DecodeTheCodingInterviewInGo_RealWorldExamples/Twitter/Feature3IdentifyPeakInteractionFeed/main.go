package main
import (
  "fmt"
)

func peakInteractionTimes(interactions []int, hours int) []int{
    temp := len(interactions) - hours + 1
    sums := make([]int, temp)
    currSum := 0
    for i := 0; i < len(interactions); i++ {
        currSum += interactions[i]
        if i >= hours {
            currSum -= interactions[i - hours]
        }
        if i >= hours - 1 {
            sums[i - hours + 1] = currSum
        }
    }
    size := len(sums)
    left := make([]int, size)
    best := 0
    for i := 0; i < len(sums); i++ {
        if sums[i] > sums[best]{
            best = i
        }
        left[i] = best
    }
    right := make([]int, size)
    best = len(sums) - 1
    for i := len(sums) - 1; i >= 0; i-- {
        if sums[i] >= sums[best] {
            best = i
        }
        right[i] = best
    }
    
    output := []int{-1, -1, -1};
    for j := hours; j < len(sums) - hours; j++ {
        i, l := left[j - hours], right[j + hours]
        if output[0] == -1 || sums[i] + sums[j] + sums[l] > sums[output[0]] + sums[output[1]] + sums[output[2]] {
            output[0] = i
            output[1] = j
            output[2] = l
        }
    }
    return output
}

func main() {
    interaction := []int{0, 2, 1, 3, 1, 7, 11, 5, 5}
    hours := 2
    print(peakInteractionTimes(interaction, hours))
}
