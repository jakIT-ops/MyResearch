package main
import (
    "fmt"
    "sort"
)

func twoProducts(itemPrices []int, i int, res [][]int) [][]int{
    seen := make(map[int]bool)

    j := i + 1
    for j < len(itemPrices) {
        complement := 200 - itemPrices[i] - itemPrices[j];
        if _, ok := seen[complement]; ok {
            res = append(res, []int{itemPrices[i], itemPrices[j], complement})
            for j + 1 < len(itemPrices) && itemPrices[j] == itemPrices[j + 1] {
                j++
            }
        }
        seen[itemPrices[j]] = true
        j++;
    }
    return res
}

func suggestThreeProducts(itemPrices []int) [][]int{
    var res [][]int
    sort.Ints(itemPrices)
    for i := 0; i < len(itemPrices); i++{
        price := itemPrices[i]
        if price > 200 {
            break
        }
        if i == 0 || itemPrices[i - 1] != price {
            res = twoProducts(itemPrices, i, res)
        }
    }
    return res
}

func main() {
    itemPrices := []int{100, 75, 150, 200, 50, 65, 40, 30, 15, 25, 60}
    print(suggestThreeProducts(itemPrices))
}
