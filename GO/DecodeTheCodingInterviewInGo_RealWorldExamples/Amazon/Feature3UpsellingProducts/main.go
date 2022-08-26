package main
import (
    "fmt"
    "math/rand"
    "time"
)

type UpsellProducts struct{
    productDict map[int]int
    productList []int
}

/** Inserts a product to the dataset. Returns true if the dataset did not already contain the specified product. */
func (up *UpsellProducts) InsertProduct(prod int) bool {
    if _, ok := up.productDict[prod]; ok {
        return false
    }
    up.productDict[prod] = len(up.productList)
    up.productList = append(up.productList, prod)
    return true
}

/** Removes a product from the dataset. Returns true if the dataset contained the specified product. */
func (up *UpsellProducts) RemoveProduct(prod int) bool{
    if _, ok := up.productDict[prod]; !ok {
        return false
    }
    last := up.productList[len(up.productList) - 1]
    index := up.productDict[prod];
    up.productList[index] = last
    up.productDict[last] = index
    up.productList = up.productList[:len(up.productList) - 1]
    delete(up.productDict, prod)
    return true;
}

/** Get a random product from the dataset. */
func (up *UpsellProducts) GetRandomProduct() int{
    return up.productList[rand.Intn(len(up.productList))];
}

func main() {
    rand.Seed(time.Now().UnixNano())
    dataset := &UpsellProducts{}
    dataset.productDict = make(map[int]int)
    dataset.InsertProduct(1212)
    dataset.InsertProduct(190)
    dataset.InsertProduct(655)
    dataset.InsertProduct(327)
    fmt.Println(dataset.GetRandomProduct())
    dataset.RemoveProduct(190)
    dataset.RemoveProduct(1212)
    fmt.Println(dataset.GetRandomProduct())
}
