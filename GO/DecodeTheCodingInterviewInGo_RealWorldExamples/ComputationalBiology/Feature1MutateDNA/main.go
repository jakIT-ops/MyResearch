package main
import "fmt"

func mutateDNA(s1, s2 string) bool {
    if s1 == s2 {
        return true
    }

    // form the graph, we can represent it as a map describing the edges
    edges := make(map[byte]byte)

    for i := 0; i < len(s1); i++ {
        
        // This clause corresponds to discovering more than one out-degree, 
        // which we concluded is not possible
        temp, ok := edges[s1[i]];
        if ok && temp != s2[i] {
            return false
        }
        
        // This corresponds to discovering a new edge
        edges[s1[i]] = s2[i];
    }

    set := make(map[byte]bool)
    for _, i := range s2{
        set[byte(i)] = true
    }
    return len(set) < 26
}


func main() {
    s1 := "aabcc"
    s2 := "ccdee"
    
    if mutateDNA(s1, s2){
        fmt.Println("Mutation Possible")
    } else {
        fmt.Println("Mutation not Possible")
    }
}
