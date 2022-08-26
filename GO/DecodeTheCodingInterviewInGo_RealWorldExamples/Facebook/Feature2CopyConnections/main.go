package main
import (
    "fmt"
)
func cloneRec(root *Node, nodesCompleted map[*Node]*Node) *Node{
    if root == nil {
      return nil
    }

    newNode := &Node{data: root.data}
    nodesCompleted[root] = newNode

    for _, p := range root.friends {
      x := nodesCompleted[p]
      if x == nil{
        newNode.friends = append(newNode.friends, cloneRec(p, nodesCompleted))
      } else {
        newNode.friends = append(newNode.friends, x)
      }
    }
    return newNode
}

func clone(root *Node) *Node{
    nodesCompleted := make(map[*Node]*Node)
    return cloneRec(root, nodesCompleted)
}

func main() {
    vertices := CreateTestGraphDirected(7, 18)

    PrintGraph(vertices[0])

    cp := clone(vertices[0])
    fmt.Println("\nAfter copy")
    PrintGraph(cp)

    set := make(map[*Node]bool)
    fmt.Println(AreGraphsEqualRec(vertices[0], cp, set))
}
