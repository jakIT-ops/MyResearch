package main
import (
  "fmt"
  "strconv"
)
func dividePosts(posts []int, k int) int {
    left := 1
    right := 0
    for _, val := range posts {
        right += val
    }
    right /= k

    for left < right {
        mid := (left + right + 1) / 2
        
        // This would denote the posts we currently have 
        // as we are traversing over the list
        target := 0
        
        // This would tell us how many days we would get after dividing 
        // the list in `mid` amount of posts
        divisions := 0;
        for _, post := range posts {
            target += post
            if target >= mid {
                divisions++
                target = 0
            }
        }
        if divisions >= k {
            left = mid
        } else {
            right = mid - 1
        }
    }
    return left
}

func main() {
    posts := []int{1000,2000,3000,4000,5000}
    nodes := 3
    fmt.Println("The master node was assigned " + strconv.Itoa(dividePosts(posts, nodes)) + " posts")

    posts = []int{6000,7000,8000,9000,10000,11000}
    nodes = 4
    fmt.Println("The master node was assigned " + strconv.Itoa(dividePosts(posts, nodes)) + " posts")
}
