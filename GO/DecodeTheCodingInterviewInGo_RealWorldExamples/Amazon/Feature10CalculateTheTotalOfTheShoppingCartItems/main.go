package main

import (
    "fmt"
    "unicode"
)

func calculateTotalAmount(data string) int {
  
    size := len(data)
    if size == 0 {
        return 0
    }
    
    st := []rune(data)
    // currentData is used to keep track of current number.
    // lastData will keep a track of last number used/evaluated.
    // total will be used to store the final result of the evaluated expression.
    var currentData, lastData, total  int = 0, 0, 0
    /* symbol is used to keep a track of operators present in a string and 
       perform the evaluation. */
    var symbol rune = '+'
    
    // currentChar allows us to iterate in a string.
    for i, currentChar := range st {

        /* First we'll check if the currentChar is a digit, if true 
           the character will be converted to an integer added to the
           currentData and then stored in currentData. */
        if unicode.IsDigit(currentChar) == true {
            currentData = (currentData * 10) + int((currentChar - '0'))
        }

        /* If currentChar is not a digit or space, we'll start 
           evaluating the given expression.  */
        if unicode.IsDigit(currentChar) == false && unicode.IsSpace(currentChar) == false || i == size - 1 {
            /* The switch is used to finally evaluate the data based on
            the operators. */
            switch symbol {
              /* If the symbol is equal to '+', the lastData will be added to the total
                 and currentData will be saved in the lastData. */
              case '+':
                total += lastData
                lastData = currentData
              /* Same goes for '-' operation, the lastData gets added to the total
                 and -currentData get saved in the lastData. */
              case '-':
                total += lastData
                lastData = -(currentData)
              /* If the symbol is  equal to '*', lastData gets multiplied with currentData
              and the result get saved in the lastData. */
              case '*':
                lastData = lastData * currentData
              /* If the symbol is  equal to '/', lastData gets divided with currentData
              and the result get saved in the lastData. */
              case '/':
                lastData = lastData / currentData
            }
            // Here symbol gets updated with the new symbol.
            symbol = currentChar
            currentData = 0
        }
    }

    // After all of the calculations lastdata is added to the total.
    total += lastData
    return total       
}

func main() {
    cartData := "2+3/7-1"
    totalAmount := calculateTotalAmount(cartData) 
    fmt.Print("Total amount of the cart is: ", totalAmount)
}
