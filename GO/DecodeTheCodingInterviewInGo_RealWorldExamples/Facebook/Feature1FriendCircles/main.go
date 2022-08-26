package main
import "fmt"

func DFS(friends [][]bool, n int, visited []bool, v int) {
    for i := 0; i < n; i++ {

        // A user is in the friend circle if he/she is friends with the user represented by
        // user index and if he/she is not already in a friend circle
        if friends[v][i] == true && !visited[i] && i != v {
            visited[i] = true;
            DFS(friends, n, visited, i);
        }
    }
}

func friendCircles(friends [][]bool, n int) int {
    if n == 0 {
        return 0
    }

    numCircles := 0     //Number of friend circles
    
    //Keep track of whether a user is already in a friend circle
    visited := make([]bool, n)
    
    //Start with the first user and recursively find all other users in his/her
    //friend circle. Then, do the same thing for the next user that is not already
    //in a friend circle. Repeat until all users are in a friend circle. 
    for i := 0; i < n; i++ {
        if (!visited[i]) {
            visited[i] = true
            DFS(friends, n, visited, i) //Recursive step to find all friends
            numCircles = numCircles + 1
        }
    }
    return numCircles
}


func main() {
    n := 4
    friends := [][]bool{{true, true, false, false}, {true, true, true, false}, {false, true, true, false}, {false, false, false, true}}
    fmt.Printf("Number of friends circles: %d\n", friendCircles(friends, n))
}
