package main
import (
  "fmt"
  "strings"
)
type Node struct{
    children map[rune]*Node
    isWord bool
}

type WordDictionary struct{
    root *Node
}

func new() WordDictionary{
    
    node := &Node{children: make(map[rune]*Node)}
    return WordDictionary{root: node}
}

func (this *WordDictionary) InsertWord(word string){
    node := this.root
    for _, c := range word{
        if _, ok := node.children[c]; !ok {
            node.children[c] = &Node{children: make(map[rune]*Node)}
        }
        node = node.children[c]
    }
    node.isWord = true;
}

func (this *WordDictionary) SearchWord(word string) bool{
    node := this.root
    for _, c := range word{
        if _, ok := node.children[c]; !ok {
          return false
        }
        node = node.children[c];
    }
    return node.isWord;
}

func (this *WordDictionary) StartsWith(word string) bool{
    node := this.root
    for _, c := range word{
        if _, ok := node.children[c]; !ok {
          return false
        }
        node = node.children[c];
    }
    return true;
}


func main() {
    // Driver Code
    keys := []string{"the", "a", "there", "answer", "any", "by", "bye", "their", "abc"}
    fmt.Println("Keys to insert: \n")
    fmt.Println(strings.Join(keys, ", "))

    d := new()

    for i := 0; i < len(keys); i++{
        d.InsertWord(keys[i])
    }
    
    fmt.Println("Searching 'there' in the dictionary results: ", d.SearchWord("there"));
    fmt.Println("Searching 'missing' in the dictionary results: ", d.SearchWord("missing"));
}
