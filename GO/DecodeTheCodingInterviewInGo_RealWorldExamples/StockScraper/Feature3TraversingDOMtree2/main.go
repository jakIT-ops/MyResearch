package main
import (
  "fmt"
)

type TreeNode struct{

    val string
    next *TreeNode
    children []*TreeNode
};

func traversingDomTree(root, prev, leftmost *TreeNode) *TreeNode {
    
    if root == nil {
        return root
    }

    leftmost = root
    
    // Variable to keep track of nodes on the "current" level
    curr := leftmost
    
    // Traverse till last node
    for leftmost != nil {
            
        // "prev" tracks the latest node on the "next" level
        // "curr" tracks the latest node on the current level
        prev = nil
        curr = leftmost
        
        leftmost = nil
        
        // Iterate on the nodes of current level like a linked list
        for curr != nil {
            fmt.Println(curr.val)

            // Process all the children and update the prev
            // and leftmost pointers as necessary.
            for _, child := range curr.children {
                // Process the child
                if child != nil {
                    
                    // If we found atleast one node on the new level,
                    // setup its next pointer
                    if prev != nil {
                        prev.next = child    
                    } else {
                        // It is the first node
                        leftmost = child
                    } 
                    prev = child;
                }
            }
            
            // Move onto the next node.
            curr = curr.next
        }
    }
    return root 
}

func main() {
    root := &TreeNode{val: "body"}
    root.children = append(root.children, &TreeNode{val: "div"})
    root.children = append(root.children, &TreeNode{val: "h1"})
    root.children = append(root.children, &TreeNode{val: "div"}) 
    root.children[0].children = append(root.children[0].children, &TreeNode{val: "h2"}) 
    root.children[0].children[0].children = append(root.children[0].children[0].children, &TreeNode{val: "ul"}) 
    root.children[0].children = append(root.children[0].children, &TreeNode{val: "h3"}) 
    root.children[0].children[1].children = append(root.children[0].children[1].children, &TreeNode{val: "a"})
    root.children[0].children[1].children = append(root.children[0].children[1].children, &TreeNode{val: "p"})
    root.children[0].children[1].children = append(root.children[0].children[1].children, &TreeNode{val: "table"}) 
    root.children[2].children = append(root.children[2].children, &TreeNode{val: "p"})
    root.children[2].children = append(root.children[2].children, &TreeNode{val: "a"})
    root.children[2].children = append(root.children[2].children, &TreeNode{val: "p"})

    traversingDomTree(root, nil, nil)
}
