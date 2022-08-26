package main
import (
    "fmt"
)

func preOrder(node *Node, low int, high int, output []int) []int{
    if node != nil {
        if (node.val <= high && low <= node.val){
            output = append(output, node.val)
        }
        if low <= node.val {
            output = preOrder(node.leftChild, low, high, output)
        }
        if node.val <= high {
            output = preOrder(node.rightChild, low, high, output)
        }
    }
    return output
}

func productsInRange(root *Node, low int, high int) []int{
    var output []int
    return preOrder(root, low, high, output)
}

func main() {
    var bst BinarySearchTree
    bst.Insert(9)
    bst.Insert(6)
    bst.Insert(14)
    bst.Insert(20)
    bst.Insert(1)
    bst.Insert(30)
    bst.Insert(8)
    bst.Insert(17)
    bst.Insert(5)
    print(productsInRange(bst.root, 7, 20))
}
