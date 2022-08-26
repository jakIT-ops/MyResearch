package main

type Stack []*TreeNode

func (s Stack) Push(v *TreeNode) Stack {
    return append(s, v)
}

func (s Stack) Pop() (Stack, *TreeNode) {
    l := len(s)
	if l == 0 {
		return s, nil
	}
    return s[:l-1], s[l-1]
}

func (s Stack) Top() *TreeNode {
    l := len(s)
	return s[l - 1]
}

func (s Stack) Empty() bool {
	return len(s) == 0
}
