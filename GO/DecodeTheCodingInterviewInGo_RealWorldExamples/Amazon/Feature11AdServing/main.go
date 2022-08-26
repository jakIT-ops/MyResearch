package main
import (
  "fmt"
)

// bufferState struct maintains the state of buff that is passed to read4()
type bufferState struct {
  buff []byte
  ptr int
  count int
}

var solution = func(read4 func(*[]byte) int) func(*[]byte, int) int {
    // implement read(n) below.
    state := &bufferState{ptr: 0,count:0} // Initializing the bufferState struct
    return func(buffer *[]byte, n int) int {
      i := 0
      for i < n { // Reading the ads list till the given n
        // If ptr is 0 call the read4() API and read 4 ads from the list of ads
        if state.ptr == 0 { 
          state.count = read4(&state.buff) // Pass the buff array by reference
        }
        // Break the loop if list of ads is empty or read4() returns 0 
        if state.count == 0{
          break;
        } 
        // Fill the buffer array using the already filled buff array
        // till the n ads.
        for i < n && state.ptr < state.count {
          // Append the ad to buffer using the append function
          *buffer = append(*buffer, state.buff[state.ptr]) 
          i++; state.ptr++;
        }
        // If ptr exceeds or reaches the count, the ptr will be set to 0
        if state.ptr >= state.count {
          state.ptr = 0
        }
      }
        return i // Return the number of ads read 
    }
}

func main(){
  
  count := 0
  buffer := []byte{}
  sol := solution(read4)

  // List of ads
  fmt.Println("Ads:",Ads)
  queries := []int{3,5,2}

  //Example 1
  fmt.Println("Example #1")
  fmt.Println("User: Read",queries[0],"ads.")
  fmt.Println("...reading",queries[0],"ads...")
  count = sol(&buffer,queries[0])
  fmt.Println("Ads count read by read(n):", count)
  fmt.Println("Ads read by read(n):", string(buffer))

  //Example 2
  fmt.Println("Example #2")
  fmt.Println("User: Read",queries[1],"ads.")
  buffer = []byte{} // Resetting the buffer
  fmt.Println("...reading",queries[1],"ads...")
  count = sol(&buffer,queries[1])
  fmt.Println("Ads count read by read(n):", count)
  fmt.Println("Ads read by read(n):", string(buffer))
  
  //Example 3
  fmt.Println("Example #3")
  fmt.Println("User: Read",queries[2],"ads")
  buffer = []byte{} // Resetting the buffer
  fmt.Println("...reading",queries[2],"ads...")
  count = sol(&buffer,queries[2])
  fmt.Println("Ads count read by read(n):", count)
  fmt.Println("Ads read by read(n):", string(buffer))
}
