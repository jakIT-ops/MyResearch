package main
import "fmt"

// Function to generate keys
func generateKey(message string) string{

    key := ""
    for i := 1; i < len(message); i++ {
        // Compute difference of adjacent characters
        diff := int(message[i]) - int(message[i-1]) 
        // Handle the wrap around case and construct the key string
        if diff < 0 {
            key += string(diff + 26)
        } else {
            key += string(diff)
        }
        key += ","
    }
    return key
}

func combineMessages(messages []string) [][]string {
    messageGroup := make(map[string][]string)

    for _, message := range messages {
        // Get key for current message
        key := generateKey(message)
        // Assign value to keys
        var list []string
        if value, ok := messageGroup[key]; ok{
            list = value
        }
        list = append(list, message);
        messageGroup[key] = list
    }
    var groups [][]string
    for _, group := range messageGroup {
        groups = append(groups, group)
    }
    return groups
}


func main() {
    // Driver code
    messages := []string{"lmn", "mno", "azb", "bac", "yza", "bdfg"}
    groups := combineMessages(messages)

    fmt.Println("The Grouped Messages are:\n")
    for _, group := range groups{
        print(group) 
    }
}
