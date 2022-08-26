package main
import (
  "fmt"
  "strings"
)

func findDuplicateTweets(tweetsInfo []string) [][]string{
  // create a hashmap to store the duplicate people names for a hashtag
  Map := make(map[string][]string)
  // iterate over each tweet information
  for j := 0; j < len(tweetsInfo); j++ {
    tweet := tweetsInfo[j]
    // obtain the days, people names, and hashtags 
    // separately by splitting based on the space
    values := strings.Split(tweet, " ")
    for i := 1; i < len(values); i++ {
      // split the person name and the hashtag appropriately to get the hashtag
      name_cont := strings.Split(values[i], "(")
      name_cont[1] = strings.Replace(name_cont[1], ")", "", -1)
      // check if the hashtag already exists in the Map
      // if it exists, then return its value and add the hashmap path to it,
      // otherwise create a new list and add the hashmap path to it
      if _, ok := Map[name_cont[1]]; !ok {
        Map[name_cont[1]] = make([]string, 0)
      }
      list := Map[name_cont[1]]
      list = append(list, values[0] + "/" + name_cont[0])
      Map[name_cont[1]] = list
    }
  }  
  // check if each hashtag has a list that consists of at least 
  // two hashtag paths, and add such lists to the output and return it
  output := make([][]string, 0)
  for key, _ := range Map {
    if len(Map[key]) > 1 {
      output = append(output, Map[key])
    }
  }
  return output
}

func main() {
  // Driver code
  tweetsInfo := []string{"Monday Joe(t20) Jack(chevrolet) Charlie(ev)", "Tuesday Alice(cake) Bob(chevrolet)", "Wednesday Joe(boeing) Jack(ev) Alice(t20)"}
  output := findDuplicateTweets(tweetsInfo)
  fmt.Println(output)
}
