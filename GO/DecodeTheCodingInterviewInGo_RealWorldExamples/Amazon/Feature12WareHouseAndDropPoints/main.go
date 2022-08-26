package main
import ( 
    "fmt" 
    "math")

/* Initializing the given constraints globally */

// OpenSpace is initialized to infinity number representing the open spacesvar EmptyBlock int = math.MaxInt32
var OpenSpace int = math.MaxInt32
// DropPoint is initialized to 0 representing the drop point
var DropPoint int = 0
/* Directions are used to keep the track of the shelves, 
   drop points and open source */
var Directions = [][]int{
    {1,0},
    {-1,0},
    {0,1},
    {0,-1} }

func warehouseAndDropPoints(warehouse [][]int){
    // First of all check if the given warehouse is empty or not
    // If empty return 
    m := len(warehouse)
    if m == 0{
        return
    }
    // Save the warehouse row and col lengths in m and n
    n := len(warehouse[0])
    // Intialize a queue to implement a Bread-First search approach
    q := new(Queue)
    // Filling the queue with drop points row, col indexes of a warehouse 
    for row := 0; row < m; row++ { 
        for col := 0; col < n; col++ {
            if warehouse[row][col] == DropPoint{
                q.Add([]int{row,col})
            }
        }
    }
    // Filling the open spaces with the distances to its nearest drop point 
    // using the queue and BFS approach
    for q.IsEmpty() == false {
        point := q.Remove()
        row := point[0]
        col := point[1]
        for i := 0; i < len(Directions); i++ {
            r := row + Directions[i][0]
            c := col + Directions[i][1]
            if r < 0 || c < 0 || r >= m || c >= n || warehouse[r][c] != OpenSpace {
                continue
            }
            warehouse[r][c] = warehouse[row][col] + 1
            q.Add([]int{r,c})
        }
    }
}

func main(){
    warehouse :=[][]int{{2147483647,-1,0,2147483647},{2147483647,2147483647,2147483647,-1},{2147483647,-1,2147483647,-1},{0,-1,2147483647,2147483647}}
    fmt.Println("Given Warehouse: ",warehouse)
    warehouseAndDropPoints(warehouse)
    fmt.Println("Filled Warehouse: ",warehouse)
}
