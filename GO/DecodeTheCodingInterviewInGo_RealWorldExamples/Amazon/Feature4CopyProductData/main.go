package main
import (
    "fmt"
    "strconv"
)

type Node struct{
    prod int
    next *Node
    related *Node
    
}

func getClonedNode(node *Node, visited map[*Node]*Node) *Node {
    if node != nil {
        if _, ok := visited[node]; ok {
            // If its in the visited hashmap then return the new node reference from the hashmap
            return visited[node]
        } else {
            // Otherwise create a new node, add to the hashmap and return it
            visited[node] = &Node{prod: node.prod}
            return visited[node]
        }
    }
    return nil
}

func copyProductRelations(head *Node, visited map[*Node]*Node) *Node{

    if (head == nil) {
      return head
    }
    oldNode := head

    // Creating the new head node.
    newNode :=  &Node{prod: oldNode.prod}
    visited[oldNode] = newNode

    // Iterate on the linked list until all nodes are cloned.
    for oldNode != nil {
      // Get the clones of the nodes referenced by related and next pointers.
      newNode.related = getClonedNode(oldNode.related, visited)
      newNode.next = getClonedNode(oldNode.next, visited)
      
      oldNode = oldNode.next
      newNode = newNode.next
    }
    return visited[head]
}


func main() {
    // Visited hashmap 
    visited := make(map[*Node]*Node)
    products := createList([]int{3, 1, 5, 4}, []int{2, 0, -1, 1})
    // The createList(values, pointer) is a utility function with parameters as: 
    // 1. values: an array of values to be stored in linked list, i.e., product IDs.
    // 2. pointer: an array containing indices of values that the "related" pointer
    // of the corresponding product will point to. 
    // This function creates the list and returns the head. 

    fmt.Println("Original list:")
    fmt.Println(listToString(products))
    // The listToString(head) function is also a utility function that returns 
    // string representation of the list.

    copiedList := copyProductRelations(products, visited)
    fmt.Println("Deep copy of list:")
    fmt.Println(listToString(copiedList))
}
 
