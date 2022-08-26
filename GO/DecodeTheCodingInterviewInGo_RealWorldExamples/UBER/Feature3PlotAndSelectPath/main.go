package main
import (
    "fmt"
)

func backtrackEvaluate(city map[string]map[string]float64, currNode string, targetNode string, accSum float64, visited map[string]bool) float64 {

	// mark the visit
	visited[currNode] = true
	ret := -1.0

	neighbors := city[currNode]
	if i, ok := neighbors[targetNode]; ok {
		ret = accSum + i
	} else {
		for nextNode, val := range neighbors {
			if _, ok := visited[nextNode]; ok {
				continue
			}
			ret = backtrackEvaluate(city, nextNode, targetNode,
					accSum + val, visited)
			if ret != -1.0 {
				break
			}
		}
	}

	// unmark the visit, for the next backtracking
	delete(visited, currNode)
	return ret
}

func getTotalCost(GMap [][]string, pathCosts []float64, drivers []string, user string) []float64 {
	
	results := make([]float64, len(drivers))
	city := make(map[string]map[string]float64)

    // Step 1). build the city from the GMap
    for i := 0; i < len(GMap); i++ {
		checkPoints := GMap[i]
		sourceNode := checkPoints[0]
		destNode := checkPoints[1]
		pathCost := pathCosts[i]

		if _, ok := city[sourceNode]; !ok {
			city[sourceNode] = make(map[string]float64)
		}
		if _, ok := city[destNode]; !ok {
			city[destNode] = make(map[string]float64)
		}

		city[sourceNode][destNode] = pathCost
		city[destNode][sourceNode] = pathCost
    }

    // Step 2). Evaluate each driver via bactracking (DFS)
    // by verifying if there exists a path from driver to user
    for i := 0; i < len(drivers); i++ {
		driver := drivers[i]
		_, temp := city[user]
		if _, ok := city[driver]; !ok || !temp { 
			results[i] = -1.0
		} else {
			visited := make(map[string]bool)
			results[i] = backtrackEvaluate(city, driver, user, 0, visited)
		}
    }
	return results
}

func main() {
	// Driver code
    GMap := [][]string{{"a","b"}, {"b","c"}, {"a","e"}, {"d","e"}}
    pathCosts := []float64{12.0,23.0,26.0,18.0}
    drivers := []string{"c", "d", "e", "f"}
    user := "a"
    print(getTotalCost(GMap, pathCosts, drivers, user))
}
