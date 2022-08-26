package main
import (
    "fmt"
    "math"
)

//This method calculates the amount of water trapped. The only argument
//passed is the elevation map, in form of an array.

func pathCost(elevationMap []int) int {
	water := 0 //keeps track of the total water as we traverse the elevation map

	n := len(elevationMap) //number of points on the map

	//lists to store the leftMax and rightMax of each point in the map
	leftMax := make([]int, n); 
	rightMax := make([]int, n) 

	//default values
	leftMax[0] = elevationMap[0]
	rightMax[n-1] = elevationMap[n-1] 

	//filling the leftMax list
	for i := 1; i < n; i++ {
		leftMax[i] = int(math.Max(float64(leftMax[i-1]), float64(elevationMap[i])))
    }
	
	//filling the rightMax list
	for i := n-2; i >= 0; i-- {
		rightMax[i] = int(math.Max(float64(rightMax[i+1]), float64(elevationMap[i]))) 
    }

	//calculating the amount of water
	for i := 0; i < n; i++ {
		water += int(math.Min(float64(leftMax[i]), float64(rightMax[i]))) - elevationMap[i]
    }

	return water
} 

func main() {
	// Driver code
	elevationMap := []int{1, 2, 1, 3, 1, 2, 1, 4, 1, 0, 0, 2, 1, 4}

	fmt.Printf("Accumulated water: %dcm", pathCost(elevationMap))
}
