package main
import "fmt"

type Node struct {
  value []int
  next *Node
}

type Queue struct {
  head *Node
  tail *Node
  size int
}

func (q *Queue) Size() int {
  return q.size
}

func (q *Queue) IsEmpty() bool {
  return q.size == 0
}

func (q *Queue) Peek() []int {
  if q.IsEmpty() {
    fmt.Println("QueueEmptyException")
    return nil
  }
  return q.head.value
}

func (q *Queue) Add(value []int) {

  temp := &Node{value, nil}
  if q.head == nil {
    q.head = temp
    q.tail = temp
  } else {
    q.tail.next = temp
    q.tail = temp
  }
  q.size++
}

func (q *Queue) Remove() []int {
 if q.IsEmpty() {
  fmt.Println("QueueEmptyException")
  return nil
 }
 value := q.head.value
 q.head = q.head.next
 q.size--
 return value
}

