package main
import "fmt"

func search(arr []int, start int, end int, key int) int{  
    if start > end {
      return -1
    }

    mid := start + (end - start) / 2

    if arr[mid] == key {
        return mid
    }

    if arr[start] <= arr[mid] && key <= arr[mid] && key >= arr[start] {
      return search(arr, start, mid - 1, key)
    } else if arr[mid] <= arr[end] && key >= arr[mid] && key <= arr[end] {
      return search(arr, mid + 1, end, key)
    } else if arr[end] <= arr[mid] {
      return search(arr, mid + 1, end, key)
    } else if arr[start] >= arr[mid] {
      return search(arr, start, mid - 1, key)
    }

    return -1
}

func findStoryId(arr []int, key int) int {
    return search(arr, 0, len(arr) - 1, key)
}

func main() {
    v1 := []int{6, 7, 1, 2, 3, 4, 5}
    fmt.Printf("Key(3) found at: %d\n", findStoryId(v1, 3))
    fmt.Printf("Key(6) found at: %d\n", findStoryId(v1, 6))

    
    v2 := []int{4, 5, 6, 1, 2, 3}
    fmt.Printf("Key(3) found at: %d\n", findStoryId(v2, 3))
    fmt.Printf("Key(6) found at: %d\n", findStoryId(v2, 6))
}
