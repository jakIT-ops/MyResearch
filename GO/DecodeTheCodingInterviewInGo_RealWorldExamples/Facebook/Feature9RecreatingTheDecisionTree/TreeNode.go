package main

type TreeNode struct{
  value string
  left *TreeNode
  right *TreeNode
}

func InitNewTreeNode() *TreeNode{
  TreeNode := new(TreeNode)
  TreeNode.value = ""
  TreeNode.left = nil
  TreeNode.right = nil
  return TreeNode
}

func NewTreeNodeUsingData(value string) *TreeNode{
  TreeNode := new(TreeNode)
  TreeNode.value = value
  TreeNode.left = nil
  TreeNode.right = nil
  return TreeNode
}

func NewTreeNodeUsingCompleteData(value string, left *TreeNode, right *TreeNode) *TreeNode{
  TreeNode := new(TreeNode)
  TreeNode.value = value
  TreeNode.left = left
  TreeNode.right = right
  return TreeNode
}
