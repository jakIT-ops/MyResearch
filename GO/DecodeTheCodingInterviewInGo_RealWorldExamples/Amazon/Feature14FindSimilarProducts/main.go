package main
import (
	"fmt"
)

func Intersection(ProductsIds1 , ProductsIds2 []int) []int {
	
	counter := make([]int, 1001)
	
	for _, id := range ProductsIds1 {
		if counter[id] == 0 {
			counter[id] = 1
		}	
	}

	for _, id := range ProductsIds2 {
		if counter[id] == 1 {
			counter[id] = 2
		}
	}

	SimilarPurchases := make([]int, 0)

	for id, count := range counter {
		if count > 1{
			SimilarPurchases = append(SimilarPurchases, id) 
		}
	}

	return SimilarPurchases
}

func main(){
	ProductsIds1 := []int{10,100,200,300,505,606,20,100,1,5}
	ProductsIds2 := []int{200,100,300,600,100,10,1,1,505,505,606,606}

	SimilarPurchases := Intersection(ProductsIds1, ProductsIds2)
	fmt.Println(SimilarPurchases)
}
