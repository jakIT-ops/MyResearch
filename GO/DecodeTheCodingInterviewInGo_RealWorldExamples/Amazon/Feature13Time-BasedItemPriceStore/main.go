package main
import (
    "sort"
    "fmt"
)

// TimeMap data structure
type TimeMap struct {
    Prices map[string][]string // Prices hash map
    TimeStamp map[string][]int // TimeStamp hash map
    
}

// TimeMap constructor
func Constructor() TimeMap {
    return TimeMap{
        Prices: make(map[string][]string),
        TimeStamp: make(map[string][]int),
    }
}

// Set TimeMap data variables
func (this *TimeMap) Set(Item string, Price string, Timestamp int)  {
    // Check if the given Item already exists in the data structure
    if _, ok := this.Prices[Item]; ok {
        // Check if the given Timestamp is in increasing order
        if Timestamp < this.TimeStamp[Item][len(this.TimeStamp[Item])-1]{
            fmt.Println("TimeStamp expected to have value from",this.TimeStamp[Item][len(this.TimeStamp[Item])-1],"to 10000000 only.")
        // Check if the given Price of an Item already exists in the data structure
        } else if Price != this.Prices[Item][len(this.Prices[Item])-1]{
            // Store Prices for the given Item in the data structure
            this.Prices[Item] = append(this.Prices[Item],Price)
            // Store Timestamp for the given Item in the data structure
            this.TimeStamp[Item] = append(this.TimeStamp[Item],Timestamp)
        } 
    } else{
        // Store Prices and Item for the given Item in the data structure
        this.Prices[Item] = append(this.Prices[Item],Price) 
        // Store Timestamp for the given Item in the data structure
        this.TimeStamp[Item] = append(this.TimeStamp[Item],Timestamp)
    }
}

// Get TimeMap data variables
func (this *TimeMap) Get(Item string, Timestamp int) string {
    // Check if the given Item is present in the data structure
    if _, ok := this.Prices[Item]; !ok {
        return "" // Return empty string if Item does not exist
    }else{
        // Find the right most occurence of the given Timestamp
        index := sort.Search(len(this.TimeStamp[Item]), 
        func(index int) bool { return this.TimeStamp[Item][index] > Timestamp }) -1
        /* If the Timestamp exist in a data structure return the Price with that
        Timestamp. */
        if index > -1{
            return this.Prices[Item][index]
        }
        // Return empty string if the Timestamp does not exists
        return ""
    }
    
        
}
// Driver code
func main(){
    
    //Example #1
    fmt.Println("Example #1")
    fmt.Println()
    obj := Constructor()
    fmt.Println("SAVE: Item = Sun Glasses ; Price = $20 ; TimeStamp = 3")
    fmt.Println()
    obj.Set("Sun Glasses","$20",3)
    fmt.Println("GET: Item = Sun Glasses ; TimeStamp = 3")
    output := obj.Get("Sun Glasses",3)
    fmt.Println("GOT: The price of Sun Glasses is:",output)
    fmt.Println()
    fmt.Println("GET: Item = Sun Glasses ; TimeStamp = 1")
    output = obj.Get("Sun Glasses", 1)
    fmt.Println("GOT: The price of Sun Glasses is:",output)
    fmt.Println()
    fmt.Println("SAVE: Item = Sun Glasses ; Price = $15, TimeStamp = 4")
    obj.Set("Sun Glasses","$15",4)
    fmt.Println()
    fmt.Println("GET: Item = Sun Glasses ; TimeStamp = 8")
    output = obj.Get("Sun Glasses", 8)
    fmt.Println("GOT: The price of Sun Glasses is:",output)
    fmt.Println()
    fmt.Println("GET: Item = Sun Glasses ; TimeStamp = 4")
    output = obj.Get("Sun Glasses", 4)
    fmt.Println("GOT: The price of Sun Glasses is:",output)
    fmt.Println()
    
    fmt.Println()
    //Example #2
    fmt.Println("Example #2")
    fmt.Println()
    obj1 := Constructor()
    fmt.Println("SAVE: Item = Watch ; Price = $30 ; TimeStamp = 5")
    obj1.Set("Watch","$30",5)
    fmt.Println()
    fmt.Println("GET: Item = Watch ; TimeStamp = 1")
    output = obj1.Get("Watch",1)
    fmt.Println("GOT: The price of Watch is:",output)
    fmt.Println()
    fmt.Println("GET: Item = Watch ; TimeStamp = 5")
    output = obj1.Get("Watch", 5)
    fmt.Println("GOT: The price of Watch is:",output)
    fmt.Println()
    fmt.Println("SAVE: Item = Watch ; Price = $25 ; TimeStamp = 2")
    obj1.Set("Watch","$25",2)
    fmt.Println()
    fmt.Println("GET: Item = Watch ; TimeStamp = 5")
    output = obj1.Get("Watch", 5)
    fmt.Println("GOT: The price of Watch is:",output)
    fmt.Println()
    fmt.Println("GET: Item = Watch ; TimeStamp = 3")
    output = obj1.Get("Watch", 3)
    fmt.Println("GOT: The price of Watch is:",output)
}
