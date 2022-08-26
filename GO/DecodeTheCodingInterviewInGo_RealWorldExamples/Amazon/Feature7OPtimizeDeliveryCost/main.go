package main
import (
    "fmt"
)

func checkDelivery(packages []int, k int) bool{
    currSum := 0
    dict := make(map[int]int)
    dict[0] = -1;
    for i := 0; i < len(packages); i++ {
        currSum += packages[i]
        if k != 0{
            currSum = currSum % k
        }
        if _, ok := dict[currSum]; ok {
            if (i - dict[currSum] > 1){
                return true
            }
        } else{
            dict[currSum] =  i
        }
    }
    return false
}

func main() {
    packages := []int{58, 42, 46, 49, 331, 26, 6, 37, 3}
    k := 10
    fmt.Println(checkDelivery(packages, k))
}
 
