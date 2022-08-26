package main
import "fmt"

func breakQuery(query string, dict []string) bool{
    dictSet := make(map[string]bool)
    for _, val := range dict{
        dictSet[val] = true
    }
    dp := make([]bool, len(query) + 1)
    dp[0] = true
    for i := 1; i <= len(query); i++ {
        for j := 0; j < i; j++ {
            if _, ok := dictSet[query[j:i]]; ok && dp[j] {
                dp[i] = true
            }
        }
    }
    return dp[len(query)]
}

func main() {
    query := "vegancookbook"
    dict := []string{"i", "cream", "cook", "scream", "ice", "cat", "book", "icecream", "vegan"};
    fmt.Println(breakQuery(query, dict))

    query = "veganicetea"
    fmt.Println(breakQuery(query, dict))
}
