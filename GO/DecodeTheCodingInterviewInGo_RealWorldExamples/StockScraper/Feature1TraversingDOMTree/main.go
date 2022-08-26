package main
import (
  "fmt"
  "container/list"
)

type TreeNode struct{

    val string
    children []*TreeNode
};

func traverse(root *TreeNode) [][]string {
    var result [][]string
    if root == nil {
        return result
    }

    queue := list.New()
    queue.PushBack(root)
    for queue.Len() != 0 {
      levelSize := queue.Len()
      var currentLevel []string
      for i := 0; i < levelSize; i++ {
          temp := queue.Front()
          queue.Remove(temp)
          currentNode := temp.Value.(*TreeNode)
          // add the node to the current level
          currentLevel = append(currentLevel, currentNode.val)
          // insert the children of current node in the queue
          for _, child := range currentNode.children {
              queue.PushBack(child)
          }
      }
      result = append(result, currentLevel)
    }
    return result
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

    print(traverse(root))
}
