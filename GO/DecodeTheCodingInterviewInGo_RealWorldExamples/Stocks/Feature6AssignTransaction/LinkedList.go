package main
import (
    "fmt"
)

type ListNode struct {
    value int
    next *ListNode
}

func Constructor(value int) *ListNode {
    node := new(ListNode)
    node.value = value
    node.next = nil
    return node
}

func (this *ListNode) DisplayOriginal(N int) int{
    fmt.Print("Original Linked List: ")
    temp := this
    for temp != nil{
        fmt.Print(temp.value, " ")
        temp = temp.next
        N++
    }
    fmt.Println(" ")
    return N
}

func (this *ListNode) DisplayReversed() {
    fmt.Print("Reversed Linked List: ");
    result := this
    for result != nil {
        fmt.Print(result.value, " ")
        result = result.next
    }
}
