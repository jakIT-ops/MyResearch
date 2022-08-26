package main
import (
  "fmt"
  "strings"
  "math"
)

/* Solution struct is used to keep the track of 
some variables instead of making them gloabl. */
type Solution struct{
  // Keeps track of index in preorder traversal.
  pIndex int
  // Storing the value -> index, in the InOrderValueIndex hashmap.
  InOrderValueIndex map[string]int
}

func (this *Solution) ReCreatingDecisionTree (preorder []string, inorder []string) *TreeNode {
  this.pIndex = 0
  // build a hashmap to store value -> its index relations
  this.InOrderValueIndex = make(map[string]int)
  for i := 0; i < len(inorder); i++ {
    this.InOrderValueIndex[inorder[i]] = i
  }
  return this.CreateTreeFromVal(preorder, 0, len(preorder) - 1)
}

func (this *Solution) CreateTreeFromVal(preorder []string, left int, right int) *TreeNode{
  // if there are no elements to construct the tree
  if left > right { 
    return nil
  }
  // select the pIndex element as the root and increment it
  rootVal := preorder[this.pIndex]
  root := NewTreeNodeUsingData(rootVal)
  this.pIndex++;
  // Constructing the left and right subtree using the root value i.e., rootVal 
  // from the InOrderValueIndex hashmap
  root.left = this.CreateTreeFromVal(preorder, left, this.InOrderValueIndex[rootVal] - 1)
  root.right = this.CreateTreeFromVal(preorder, this.InOrderValueIndex[rootVal] + 1, right)
  return root
}

func main() {
  // Driver code
  preorder := []string{"subject", "viewed", "notviewed", "similar", "nonsimilar"}
  inorder := []string{"viewed", "subject", "similar", "notviewed", "nonsimilar"}
  sol := Solution{}
  result := sol.ReCreatingDecisionTree(preorder, inorder);
  DisplayTree(result) //We're using custom helper function to print the tree
}
