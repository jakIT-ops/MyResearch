package main
import (
  "fmt"
)

func dfs( graph [][]int, color []int, currColor int, node int) bool{
    if color[node] != 0 {
        return color[node] == currColor
    }       
    color[node] = currColor;      
    for i := 0; i < len(graph[node]); i++ {
        if !dfs(graph, color, -currColor, graph[node][i]) {
            return false
        }
    }
    return true
}

func isSplitPossible(graph [][]int) bool {
    color := make([]int, len(graph))

    for i := 0; i < len(graph); i++ {             
        if color[i] == 0 && !dfs(graph, color, 1, i) {
            return false
        }
    }
    return true
}
func main() {
    graph := [][]int{{3}, {2, 4}, {1}, {0, 4}, {1, 3}}
    fmt.Println(isSplitPossible(graph))
}
