package main
import "fmt"

func suggestTwoProducts(itemPrices []int, amount int) (int, int){
    buffDict := make(map[int]int)
    for i := 0; i < len(itemPrices); i++ {
        price := itemPrices[i]
        remaining := amount - itemPrices[i]
        if _, ok := buffDict[remaining]; !ok {
            buffDict[price] = i;
        } else{
            return buffDict[remaining], i
        }
    }
    return 0, 0
}

func main() {
    itemPrices:= []int{2, 30, 56, 34, 55, 10, 11, 20, 15, 60, 45, 39, 51}
    amount := 61
    first, second := suggestTwoProducts(itemPrices, amount)
    fmt.Printf("%d, %d\n", first, second)
}
