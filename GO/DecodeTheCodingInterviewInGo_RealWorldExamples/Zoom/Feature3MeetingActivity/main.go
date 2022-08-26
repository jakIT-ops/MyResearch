package main
import "fmt"

func minSteps(k []int) int {
    n := len(k)
    if n <= 1 {
        return 0
    }

    graph := make(map[int][]int)
    for i := 0; i < n; i++ {
        if _, ok := graph[k[i]]; ok{
            graph[k[i]] = []int{i}
        } else {
            graph[k[i]] = append(graph[k[i]], i)
        }
    }

    current := []int {0}// store current layer

    visited := make(map[int]bool)
    step := 0

    // when current layer exists
    for len(current) != 0 {
        var nextNode []int

        // iterate the layer
        for _, node := range current {
            // check if reached end
            if node == n - 1 {
                return step
            }

            // check same value
            for _, child := range graph[k[node]] {
                if _, ok := visited[child]; !ok {
                    visited[child] = true
                    nextNode = append(nextNode, child)
                }
            }

            // clear the list to prevent redundant search
            graph[k[node]] = []int{}

            // check neighbors
            
            if _, ok := visited[node + 1]; !ok &&  node + 1 < n{
                visited[node + 1] = true
                nextNode = append(nextNode ,node + 1)
            }
            if  _, ok := visited[node - 1]; !ok && node - 1 >= 0{
                visited[node - 1] = true
                nextNode = append(nextNode ,node - 1)
            }
        }

        current = nextNode
        step++
    }

    return -1
}

func main() {
    k := []int{1, 2, 3, 4, 1, 3, 5, 3, 5}
    fmt.Println(minSteps(k))
}
