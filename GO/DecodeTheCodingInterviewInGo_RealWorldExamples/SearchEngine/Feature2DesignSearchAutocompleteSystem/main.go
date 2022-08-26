package main
import (
  "fmt"
  "sort"
  
)

type Node struct{ 
    children map[rune]*Node
    isEnd bool
    data string
    rank int
    hot []*Node
}

func (this *Node) Update(n *Node){
    nd := sort.Search(len(this.hot), func(i int) bool {return this.hot[i] == n}) 
    if nd <= len(this.hot) {
        this.hot = append(this.hot, n)
    }
    sort.Slice(this.hot, func(i, j int) bool {
        return this.hot[i].rank > this.hot[j].rank
    })
    if (len(this.hot) > 3) {
        this.hot = this.hot[:len(this.hot) - 1]
    }
}

type AutoCompleteSystem struct{

    root *Node
    current *Node
    keyword string
}

func new(sentences []string, times []int) *AutoCompleteSystem {

    root := &Node{children: make(map[rune]*Node)}
    
    AutoCompleteSystem := &AutoCompleteSystem{root: root, current: root}
    for i := 0; i < len(sentences); i++{
        AutoCompleteSystem.AddRecord(sentences[i], times[i]);
    }
    return AutoCompleteSystem
}

func (this *AutoCompleteSystem) AddRecord(sentence string, t int){
    node := this.root
    var visited []*Node
    for _, c := range sentence {
        if _, ok := node.children[c]; !ok {
            node.children[c] = &Node{children: make(map[rune]*Node)}
        }
        node = node.children[c]
        visited = append(visited, node)
    }
    node.isEnd = true
    node.data = sentence
    node.rank += t

    for _, i := range visited{
        i.Update(node)
    }
}

func (this *AutoCompleteSystem) AutoComplete(c rune) []string{
    var res []string
    if (c == '#') {
        this.AddRecord(this.keyword, 1)
        this.keyword = ""
        this.current = this.root
        return res
    }
    
    this.keyword += string(c)
    if this.current != nil {
        if _, ok := this.current.children[c]; !ok {
            return res
        } else{
            this.current = this.current.children[c]
        }
    } else {
        return res
    }
    
    for _, node := range this.current.hot {
        res = append(res, node.data)
    }
    return res
}


func main() {

    sentences := []string{"beautiful", "best quotes", "best friend", "best birthday wishes", "instagram", "internet"};
    times := []int{30, 14, 21, 10, 10, 15};
    autoComplete := new(sentences, times);
    print(autoComplete.AutoComplete('b'))
    print(autoComplete.AutoComplete('e'))
    print(autoComplete.AutoComplete('s'))
    print(autoComplete.AutoComplete('t'))
    print(autoComplete.AutoComplete('#'))
}
