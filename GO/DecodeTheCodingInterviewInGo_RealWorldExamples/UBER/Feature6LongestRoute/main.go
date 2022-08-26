package main
import (
    "fmt"
    "math"
)

type TreeNode struct {
    val string
    left *TreeNode
    right *TreeNode
}

func height(node *TreeNode) int {
  if node == nil {
      return 0
  } else{
    // Compute the height of each subtree
    lh := height(node.left)
    rh := height(node.right)

    // Use the larger one 
    return int(math.Max(float64(lh), float64(rh))) + 1
  }
}

func longestRoute(root *TreeNode) int{
    if root == nil {
        return 0
    }
    
    lHeight := height(root.left)
    rHeight := height(root.right)

    lPath := longestRoute(root.left)
    rPath := longestRoute(root.right)

    temp := math.Max(float64(lPath), float64(rPath))
    res := int(math.Max(float64(lHeight + rHeight + 1), temp))

    return res
}


func main() {
    // Driver code

  root := &TreeNode{val: "a"}
  root.left = &TreeNode{val: "b"}
  root.right = &TreeNode{val: "c"}
  root.left.left = &TreeNode{val: "d"}
  root.right.left = &TreeNode{val: "e"}
  root.right.right = &TreeNode{val: "f"}
  fmt.Printf("The longest route will pass through %v checkpoints", longestRoute(root))
}
