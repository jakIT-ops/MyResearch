package main
import (
    "fmt"
    "reflect"
)

func findSimilarity(products []int, candidates []int) []int{
    prodN := len(products)
    candN := len(candidates)
    var output []int
    if prodN < candN{
        return output;
    }

    candCount := make(map[int]int)
    prodCount := make(map[int]int)
  
    for _, i := range candidates {
        if _, ok := candCount[i]; ok {
            candCount[i] = candCount[i] + 1
        } else {
            candCount[i] = 1
        }
    }
    for i := 0; i < prodN; i++ {
        k := products[i]
        if _, ok := prodCount[k]; ok {
            prodCount[k] = prodCount[k] + 1
        } else {
            prodCount[k] = 1
        }
        
        if i >= candN {
            k = products[i - candN];
            if prodCount[k] == 1 {
                delete(prodCount, k)
            } else {
                prodCount[k] = prodCount[k] - 1
            }
        }
        
        if reflect.DeepEqual(candCount, prodCount) {
            output = append(output, i - candN + 1)
        }
    }
    return output
}

func main() {
    products := []int{3, 2, 1, 5, 2, 1, 2, 1, 3, 4}
    candidates := []int{1, 2, 3}
    print(findSimilarity(products, candidates))
}
 
