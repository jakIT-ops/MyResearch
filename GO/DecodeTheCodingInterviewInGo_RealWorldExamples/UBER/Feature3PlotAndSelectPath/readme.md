## Description

After obtaining the closest drivers and calculating the cost of traveling on different roads, we need to build a functionality to select a path from the driver’s location to the user’s location. All the drivers have to pass through multiple checkpoints to reach the user’s location. Each road between checkpoints will have a cost, which we learned how to calculate in the previous lesson. It is possible that some of the k chosen drivers might not have a path to the user due to unavailability. Unavailability can occur due to a driver already being in a ride that has ended but not reached its location. In some cases, the driver can also get booked by another user and become unavailable. The driver that has the path to the user’s location with the minimum accumulated cost will be selected.

We’ll be given a city map GMap as a list of different checkpoints. Another list pathCosts, at each index, will represent the cost of traveling between the corresponding checkpoints in GMap. We are also given some drivers, where each drivers[i] represents a single driver node. We need to determine whether a path from the driver node drivers[i] to a user node exists or not. If the path exists, return the accumulated sum of the checkpoints between the two nodes. Otherwise, return -1.

## Solution

The main problem comes down to finding a path between two nodes, if it exists. If the path exists, return the cumulative sums along the path as the result. Given the problem, it seems that we need to track the nodes where we come from. DFS (Depth-First Search), also known as the backtracking algorithm, will be applicable in this case.

Here is how the implementation will take place:

1. Build the graph using the city map list GMap.

2. Assign the cost to each edge while building the graph.

3. Once the graph is built, evaluate each driver’s path in the drivers list by searching for a path between the driver node and the user node.

4. Return the accumulated sum if the path exists. Otherwise, return -1.







