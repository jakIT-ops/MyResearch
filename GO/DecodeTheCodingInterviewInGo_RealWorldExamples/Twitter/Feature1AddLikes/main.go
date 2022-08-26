package main
import (
  "fmt"
  "strconv"
)
func addLikes(like1, like2 string) string{
    res := ""

    carry, p1, p2 := 0, len(like1) - 1, len(like2) - 1
    for p1 >= 0 || p2 >= 0 {
        var x1, x2 int
        if p1 >= 0 {
            x1 = int(like1[p1] - '0')
        } else {
            x1 = 0;
        }
        if p2 >= 0 {
            x2 = int(like2[p2] - '0')
        } else {
            x2 = 0
        }
        value := (x1 + x2 + carry) % 10
        carry = (x1 + x2 + carry) / 10
        res += strconv.Itoa(value)
        p1--
        p2--;   
    }
    
    if carry != 0 {
        res += strconv.Itoa(carry)
    }
    // reverse the string
    runes := []rune(res)
    for i, j := 0, len(runes) - 1; i < j; i, j = i + 1, j-1 {
      runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes);
}

func main() {
    fmt.Println(addLikes("1545", "67"))
}
