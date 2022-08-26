package main
import (
    "fmt"
    "math"
)
// returns size of the current/latest palindrome
func returnPalindromeLength(s string, left int, right int) int{
    for left >= 0 && right < len(s) && s[left] == s[right] {
        left--
        right++
    }

    return right - left - 1
}

func locateProtein(s string) string {
    if (len(s) < 1) {
        return ""
    }
    start, end := 0, 0

    for i := 0; i < len(s); i++ {

        len1 := returnPalindromeLength(s, i, i) // for odd length
        len2 := returnPalindromeLength(s, i, i + 1) // for even length
        len := int(math.Max(float64(len1), float64(len2)))

        if len > end - start {
            start = i - (len - 1) / 2
            end = i + len / 2
        }
    }

    return s[start: end + 1]
}

func main() {
    // Driver code
    sequence := "aaccbababcbc"
    fmt.Println(locateProtein(sequence))
}
