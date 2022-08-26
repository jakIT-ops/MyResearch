package main


type Node struct{
    val int
    leftChild *Node
    rightChild *Node
}

func (n *Node) Insert(val int) {
    current := n
    parent := current
    for current != nil {
        parent = current
        if val < current.val{
            current = current.leftChild
        } else {
            current = current.rightChild
        }
    }
    if val < parent.val {
        parent.leftChild = &Node{val: val}
    } else {
        parent.rightChild = &Node{val: val}
    }
}

type BinarySearchTree struct{
    root *Node
}


func (b *BinarySearchTree) Insert(val int){
    if b.root == nil {
        b.root = &Node{val: val}
    } else {
        b.root.Insert(val)
    }
}
