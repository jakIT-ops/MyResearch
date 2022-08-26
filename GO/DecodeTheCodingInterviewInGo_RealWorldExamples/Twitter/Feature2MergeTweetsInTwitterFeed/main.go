package main
import (
  "fmt"
)

func mergeTweets(feed *[]int, m int, tweets []int, n int) {
    p1 := m - 1
    p2 := n - 1
    
    for p := m + n - 1; p >= 0; p-- {
        if p2 < 0 {
            break
        }
        if p1 >= 0 && (*feed)[p1] > tweets[p2] {
            (*feed)[p] = (*feed)[p1]
            p1--
        } else {
            (*feed)[p] = tweets[p2]
            p2--
        }
    }
}

func main() {
    feed := []int{23, 33, 35, 41, 44, 47, 56, 91, 105, 0, 0, 0, 0, 0, 0}
    tweets := []int{32, 49, 50, 51, 61, 99}
    m, n := 9, 6
    mergeTweets(&feed, m, tweets, n)
    print(feed)
}
