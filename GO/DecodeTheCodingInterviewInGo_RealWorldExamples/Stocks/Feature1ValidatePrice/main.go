package main
import "fmt"

type STATE int

const ( 
  START STATE = iota
  INTEGER
  DECIMAL 
  UNKNOWN 
  AFTERDECIMAL
)

func getNextState(currentState STATE, ch byte) STATE {
  switch currentState {
    case START, INTEGER:
      if ch == '.' {
        return DECIMAL
      } else if ch >= '0' && ch <= '9' {
        return INTEGER
      } else {
        return UNKNOWN;
      }
    case DECIMAL:
      if (ch >= '0' && ch <= '9') {
        return AFTERDECIMAL;
      } else {
        return UNKNOWN;
      }
    case AFTERDECIMAL: 
      if (ch >= '0' && ch <= '9') {
        return AFTERDECIMAL;
      } else {
        return UNKNOWN;
      }
  }
  return UNKNOWN;
}

func isPriceValid(s string) bool {
    if len(s) == 0 {
        return true
    }
    i := 0
    if s[i] == '+' || s[i] == '-' {
        i++

        var currentState STATE = START
        for i < len(s) {
            currentState = getNextState(currentState, s[i])
            if currentState == UNKNOWN {
                return false
            }

            i++
        }
        
        if currentState == DECIMAL {
            return false
        }
        
        return true
    }
    return false
}

func main() {
    fmt.Printf("Is the price valid +40.325? %v\n", isPriceValid("+40.325"))
    fmt.Printf("Is the price valid -1.1.1? %v\n", isPriceValid("-1.1.1"))
    fmt.Printf("Is the price valid -222? %v\n", isPriceValid("-222"))
    fmt.Printf("Is the price valid ++22? %v\n", isPriceValid("++22"))
    fmt.Printf("Is the price valid 10.1? %v\n", isPriceValid("10.1"))
    fmt.Printf("Is the price valid 22.22.? %v\n", isPriceValid("22.22."))
    fmt.Printf("Is the price valid .100? %v\n", isPriceValid(".100"))
}
