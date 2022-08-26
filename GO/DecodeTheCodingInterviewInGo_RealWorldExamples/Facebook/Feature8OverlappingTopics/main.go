package main
import (
  "fmt"
)

func smallestSequence(listA []string, listB []string) []string{
  // Returns an empty list if one or more list is empty.
  if len(listA) == 0 || len(listB) == 0 {
    return make([]string, 0)
  }
  // We will use this hashmap to keep a count of all unique topics in listB.
  dictListB := make(map[string]int)
  for i := 0; i < len(listB); i++ {
    count := 0
    if _, ok := dictListB[listB[i]]; !ok{
      dictListB[listB[i]] = 0
    }
    count = dictListB[listB[i]]
    dictListB[listB[i]] = count + 1
  }

  // This will hold the count of number of unique topics in listB.
  countUniqueB := len(dictListB)

  // uniqueCharacters keeps a count of the number of unique characters of listB which are present in the current with its required frequency.
  uniqueCharacters := 0

  // This hashmap holds the count of all the unique topics in the current window.
  uniqueTopics := make(map[string]int)

  // Checks and appends a topic along with its index from list A in sifted list, if the topic is present in listB.
  siftedListA := make([]map[int]string, 0)
  for i := 0; i < len(listA); i++ {
    str := listA[i]
    if _, ok := dictListB[str]; ok {
      tempMap := make(map[int]string)
      tempMap[i] = str
      siftedListA = append(siftedListA, tempMap)
    }
  }
  // An array that is used to store the window length, left, right
  tupleWllr := []int{-1, 0, 0}

  // Left and right pointers
  left, right := 0, 0

  // Look for the topics only in the filtered list instead of entire list.
  for right < len(siftedListA) {
    // Add one topic from the right to the window
    topic := ""
    for _, t := range siftedListA[right]{
      topic = t
    }

    count := 0
    if _, ok := uniqueTopics[topic]; !ok{
      uniqueTopics[topic] = 0
    }
    count, _ = uniqueTopics[topic]
    uniqueTopics[topic] = count + 1

    // Checking the frequency of the currently added topic.
    // If it is equal to the desired count in our listB then we are incrementing the value of uniqueCharacters.
    if _, ok := dictListB[topic]; ok && uniqueTopics[topic] == dictListB[topic] {
      uniqueCharacters++
    }
    
    // If the current window has all the topics in desired frequencies i.e. it is present in the window
    for left <= right && uniqueCharacters == countUniqueB {
      for _, t := range siftedListA[left]{
        topic = t
      }
      // Save the smallest window until now.
      endSequence := 0
      startSequence := 0
      for key, _ := range siftedListA[right]{
        endSequence = key
      }
      for key, _ := range siftedListA[left]{
        startSequence = key
      }

      if tupleWllr[0] == -1 || endSequence - startSequence + 1 < tupleWllr[0] {
        tupleWllr[0] = endSequence - startSequence + 1
        tupleWllr[1] = startSequence
        tupleWllr[2] = endSequence
      }
      // The character at the position pointed by the `left` pointer is no longer a part of the window.
      num, _ := uniqueTopics[topic]
      uniqueTopics[topic] =  num - 1
      if _, ok := dictListB[topic]; ok && uniqueTopics[topic] < dictListB[topic] {
        uniqueCharacters--;
      }

      // Moving the left pointer ahead.
      left++
    }

    // Moving the right pointer ahead.
    right++
  }

  if tupleWllr[0] == -1 {
    return make([]string, 0)
  } else {
    res := make([]string, (tupleWllr[2] + 1) -  tupleWllr[1])
    for j, i := 0, tupleWllr[1]; i < tupleWllr[2] + 1; i++ {
      res[j] = listA[i]
      j++
    }
    return res
  }
}

func main() {
  // Driver code
  A := []string{"corona","petrol","corona","corona","climate","petrol","corona","petrol"}
  B := []string{"corona","petrol","climate"}

  out := smallestSequence(A, B)
  fmt.Println(out)
}
