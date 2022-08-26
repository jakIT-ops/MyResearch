package main
import (
  "fmt"
)

type TreeNode struct{
    val int
    children []*TreeNode
};

func lowestCommonAncestor(root, a, b *TreeNode) int{
    var stack Stack
    parent := make(map[*TreeNode]*TreeNode)

    parent[root] = nil
    stack = stack.Push(root)
    _, temp := parent[b]
    _, ok := parent[a]
    for !ok || !temp {
        node := stack.Top()
        stack, _ = stack.Pop();

        // Save the parent pointers while iterating
        for _, child := range node.children {
            parent[child] = node
            stack = stack.Push(child)
        }
        _, temp = parent[b]
        _, ok = parent[a]
    }

    ancestors := make(map[*TreeNode]bool)

    for a != nil {
        ancestors[a] = true
        a = parent[a]
    }

    // The first ancestor of b which appears in
    // a's ancestor set() is their lowest common ancestor.
    _, ok = ancestors[b]
    for !ok {
        b = parent[b]
        _, ok = ancestors[b]

    }
    
    return b.val
}

func main() {
    root := &TreeNode{val: 1}
    root.children = append(root.children, &TreeNode{val: 2})
    root.children = append(root.children, &TreeNode{val: 3})
    root.children = append(root.children, &TreeNode{val: 4}) 
    root.children[0].children = append(root.children[0].children, &TreeNode{val: 5}) 
    root.children[0].children[0].children = append(root.children[0].children[0].children, &TreeNode{val: 10}) 
    root.children[0].children = append(root.children[0].children, &TreeNode{val: 6}) 
    root.children[0].children[1].children = append(root.children[0].children[1].children, &TreeNode{val: 11})
    root.children[0].children[1].children = append(root.children[0].children[1].children, &TreeNode{val: 12})
    root.children[0].children[1].children = append(root.children[0].children[1].children, &TreeNode{val: 13}) 
    root.children[2].children = append(root.children[2].children, &TreeNode{val: 7})
    root.children[2].children = append(root.children[2].children, &TreeNode{val: 8})
    root.children[2].children = append(root.children[2].children, &TreeNode{val: 9})

    a := root.children[0].children[1].children[2]
    b := root.children[0].children[0].children[0]
    fmt.Printf("\"%v\" is the lowest common ancestor of the nodes \"%v\" and \"%v\"\n", lowestCommonAncestor(root, a, b), a.val, b.val)


    c := root.children[0]
    d := root.children[2].children[0]
    fmt.Printf("\"%v\" is the lowest common ancestor of the nodes \"%v\" and \"%v\"\n", lowestCommonAncestor(root, c, d), c.val, d.val)
}
