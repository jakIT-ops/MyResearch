package main

type MaxHeap []Location

func (h MaxHeap) Len() int           { return len(h) }
func (h MaxHeap) Empty() bool           { return len(h) == 0 }

func (h MaxHeap) Less(i, j int) bool { return h[i].distFromOrigin() < h[j].distFromOrigin() }
func (h MaxHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h MaxHeap) Top() Location     { return h[0] }

func (h *MaxHeap) Push(x interface{}) {
	*h = append(*h, x.(Location))
}

func (h *MaxHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}
