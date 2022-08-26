package main
import (
  "fmt"
  "math"
)

func ReverseTransactions(Head *ListNode, t int) *ListNode{
  ptr := Head // a pointer to traverse the original list.
  tTail := new(ListNode) 
  tTail = nil 
  // Head of the final list that we need to return as the output.
  NewHead := new(ListNode) 
  NewHead = nil
  // Keep traversing until there are nodes in the list
  for ptr != nil {
    count := 0  
    // Start counting nodes from the Head
    ptr = Head  
    // Count the first t nodes.
    for count < t && ptr != nil {
      ptr = ptr.next
      count += 1
    }
    // If we counted t nodes, then we reverse them.   
    if (count == t) {
        // Reverse these t nodes and get the new Head of the reversed list
      RevHead := Reverse(Head, t)  
      // NewHead is the Head of the final linked list
      if (NewHead == nil) {
        NewHead = RevHead
      }    
      // the tTail node of the previous t nodes after reversal.
      if (tTail != nil) {
        tTail.next = RevHead
      }      
      tTail = Head
      Head = ptr
    }
  }       
  // if any nodes are not reveresed, then attack them to the reversed list
  if (tTail != nil) {
    tTail.next = Head
  }
  if NewHead == nil {
    return Head
  } else {
    return NewHead
  }
}

// Assume that the linked list has at least t nodes.
// Reverse t nodes of the given linked list.
func Reverse(Head *ListNode, t int) *ListNode{
  NewHead := new(ListNode)
  NewHead = nil
  ptr := Head // a pointer to traverse the original list.  
  for (t > 0) {
    // Track the next node to traverse in the original list
    NextNode := ptr.next    
    // At the beginning of the reversed list,
    // insert the node pointed to by `ptr`
    ptr.next = NewHead
    NewHead = ptr    
    // Move on to the next node
    ptr = NextNode    
    // Decrement the count of nodes to be reversed by 1
    t--
  }       
  // Return reversed list's Head
  return NewHead
}

func main() {
  Head := Constructor(1)
  Head.next = Constructor(2)
  Head.next.next = Constructor(3)
  Head.next.next.next = Constructor(4)
  Head.next.next.next.next = Constructor(5)
    
  N := Head.DisplayOriginal(0) // number of stock transaction requests

  K := 2 // number of brokers
  t := int(math.Floor(float64(N/K)))
  if (t <= 0) {
    fmt.Print("The expected 't' to have value from 1 to length of the linked list only.");
  } else {
      RevHead := ReverseTransactions(Head, t);
      RevHead.DisplayReversed();
  }
}
