package main
import (
  "fmt"
)


type Node struct {
    start int
    end int
    leftChild *Node
    rightChild *Node
}

type BST struct {
    root *Node
}

func (b *BST) Insert(start, end int) bool {
    
    if b.root == nil {
        b.root = &Node{start: start, end: end}
        return true
    }
    newNode := &Node{start: start, end: end}
    return b.AddNode(b.root, newNode)
}

func (b *BST) AddNode(currentNode, newNode *Node) bool {
    if newNode.start >= currentNode.end {
        if currentNode.rightChild == nil {
            currentNode.rightChild = newNode
            return true
        }
        return b.AddNode(currentNode.rightChild, newNode)
    } else if newNode.end <= currentNode.start {
        if currentNode.leftChild == nil{
            currentNode.leftChild = newNode
            return true
        }
        return b.AddNode(currentNode.leftChild, newNode)
    } else {
        return false
    }
}

func checkMeeting(meetingTimes [][]int, newMeeting []int) bool{
    tree := &BST{}
    for _, meeting := range meetingTimes {
        tree.Insert(meeting[0], meeting[1])
    }
    return tree.Insert(newMeeting[0], newMeeting[1])
}

func main() {
    meetingTimes := [][]int{{1, 3}, {4, 6}, {8, 10}, {10, 12}, {13, 15}}
    
    newMeeting := []int{7, 8}
    fmt.Println(checkMeeting(meetingTimes, newMeeting))
    
    newMeeting2 := []int{9, 11}
    fmt.Println(checkMeeting(meetingTimes, newMeeting2))
}
