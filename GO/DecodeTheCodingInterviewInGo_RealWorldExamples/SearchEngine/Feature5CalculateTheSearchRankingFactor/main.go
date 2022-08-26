package main
import "fmt"

func searchRanking(pageScores []int) []int{
    length := len(pageScores)
    ranking := make([]int, length)
    ranking[0] = 1
    for i := 1; i < length; i++{
        ranking[i] = pageScores[i - 1] * ranking[i - 1]
    }
    
    right := 1
    for i := length - 1; i >= 0; i--{
        ranking[i] = ranking[i] * right
        right *= pageScores[i]
    }
    return ranking
}

func main() {
    pageScores := []int{3, 5, 1, 1, 6, 7, 2, 3, 4, 1, 2}
    print(searchRanking(pageScores))
}
