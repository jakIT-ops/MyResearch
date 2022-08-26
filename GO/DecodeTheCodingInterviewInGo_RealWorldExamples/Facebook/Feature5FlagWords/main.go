package main
import "fmt"

func repeatedLetters(s string, ind int) int{
    temp := ind
    for temp < len(s) && s[temp] == s[ind] {
        temp++
    }
    return temp - ind
}

func flagWords(S, W string) bool{
    if len(S) == 0 || len(W) == 0 {
        return false
    }
    i, j := 0, 0
    for i < len(S) && j < len(W) {
        if S[i] == W[j] {
            len1 := repeatedLetters(S, i)
            len2 := repeatedLetters(W, j)
            if len1 < 3 && len1 != len2 || len1 >= 3 && len1 < len2 {
                return false
            }
            i += len1
            j += len2
        } else {
            return false
        }
    }
    return i == len(S) && j == len(W)
}

func main() {
    S := "mooooronnn"; // modified word
    W := "moron"; // original word
    
    if flagWords(S, W){
        fmt.Println("Word Flagged")
        fmt.Println("The Word \"" + S + "\"" + " is a possible morph of \"" + W + "\"")
    } else {
        fmt.Println("Word Safe")
    }
}
