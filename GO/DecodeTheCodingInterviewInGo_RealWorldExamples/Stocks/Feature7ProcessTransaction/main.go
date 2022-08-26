package main
import (
  "fmt"
  "math"
)

func ProcessLog(s string) int{
  length := len(s);
  isSpace := false;
  // sanity check if the length of the string is 0, simply return 0
  if length == 0 {
    return 0
  }
  index := 0
  // 1. check for white spaces
  // Only the space character ' ' is considered a whitespace character.
  for index < len(s) && s[index] == ' ' {
    index++
    isSpace = true
  }

  if index == len(s) && isSpace {
    return 0;
  }

  // 2. check sign
  isNegative := 0  
  if s[index] == '-' {
      isNegative = 1
      index++
  } else if s[index] == '+' {
    index++
  }
  // 3. read until next non-digit character found
  result := 0
  for i := index; i < length; i++ {
    // check if the current character is a non-digit character is not
    if s[i] >= '0' && s[i] <= '9' {
      /* s[i] - '0' is to convert the char digit into int digit 
      eg: '9' - '0' --> 9
      or else we will be storing the ASCII value of 9 i.e. 57,
      so we do 57(ASCII of 9) - 48(ASCII of 0(zero)) to get 9 as int*/
      charToDigitVal := s[i] - '0'
      // 4. check range (integer underflow and overflow)
      if result > (math.MaxInt64 / 10) || (result == (math.MaxInt64 / 10) && charToDigitVal > 7) {
        if(isNegative == 0) {
          return math.MaxInt64
        } else {
          return math.MinInt64
        }
      }
      // adding digits at their desired place-value
      result = (result * 10) + int(charToDigitVal)
      index++
    } else {
      break
    }
  }
  if isNegative == 1 {
    return -result
  } else {
    return result
  }
}

func main() {
  s := []string{"42", "    -123", "-42", "42 with words", "word 42", "1", " "} 
  for i := 0; i < len(s); i++ {
    val := ProcessLog(s[i])
    fmt.Println(val);
  }
}
