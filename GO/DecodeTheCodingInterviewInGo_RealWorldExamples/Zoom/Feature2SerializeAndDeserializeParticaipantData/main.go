package main
import (
    "fmt"
    "strings"
)

func serialize(root *Node) string{
    var res []string
    str := ""
    res = preOrder(root, res)
    for i := 0; i < len(res); i++{
        str += res[i]
        if i + 1 < len(res){
            str += ","
        }
    }
    return str
}

func preOrder(root *Node, res []string) []string{
    if root != nil {
        res = append(res, root.val)
        res = preOrder(root.leftChild, res)
        res = preOrder(root.rightChild, res)
    }
    return res
}

func deserialize(data string) *Node{
    var root *Node
    delim := ","
    
    lst := strings.Split(data, delim)

    var stack Stack
    for _, name := range lst{
        if root == nil {
            root = &Node{val: name}
            stack = stack.Push(root)
        } else{
            root.Insert(name)
        }
    }
    return root
}

func main() {
    var bst BinarySearchTree
    names := []string{"Jeanette", "Elia", "Albert", "Latasha", "Elvira", "Kandice", "Maggie"};
    for _, name := range names{
        bst.Insert(name)
    }
    fmt.Println("Original BST:")
    printTree(bst.root)
  
  
    str := serialize(bst.root)
    fmt.Println("\nSerialized: ", str)

    deserialized := deserialize(str)
    fmt.Println("\nDeserialized:")
    printTree(deserialized)
}
