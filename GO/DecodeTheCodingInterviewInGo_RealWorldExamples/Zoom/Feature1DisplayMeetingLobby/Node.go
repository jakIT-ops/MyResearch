package main

type Node struct{
    val string
    leftChild *Node
    rightChild *Node
}

func (n *Node) Insert(val string) {
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
