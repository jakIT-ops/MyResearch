## Description

In this feature, the company has decided that they want to show people “follow” recommendations. For this purpose, we have been given the “following” relationship information for a group of users in the form of a graph. We want to see if these people can be split into two groups such that no one in the group follows or is followed-by anyone in the same group. We will then recommend people from the same group to each other.

The “following” relationship graph is given in the form of an undirected graph. So, if UserA follows UserB, or the other way around, it does not matter. This graph will be given to you as an input in the form of a 2D array called graph. In this array, each graph[i] will contain a list of indices, j, for which the edge between nodes i and j exists. Each node in the graph will represent a person and will be denoted by an integer ID from 0 to len(graph)-1.

## Solution

As mentioned above, a graph that can be split is also called a bipartite graph. To check if a graph is bipartite, we will color a node blue if it is part of the first set; otherwise, we will color it red. We can color the graph greedily if and only if it is bipartite. In a bipartite graph, all of a blue node’s neighbors must be red, and all of a red node’s neighbors must be blue.

The complete algorithm is given below:

* We’ll keep an array or HashMap to store each node’s color as color[node]. The possible values for colors can be 0, 1, or uncolored (-1 or nil).

* We will search each node in the graph to ensure disconnected nodes are also visited. For each uncolored node, we’ll start the coloring process by doing DFS on that node.

* To perform DFS, we will first check if the nodes connected to the current node are colored or not. If a node is colored, we will check if the color is the same color as the current node. If the colors are the same, we return false.

* If the node is not colored, we will color it and call DFS on that node recursively. If the recursive call returns false, the current DFS should also return false because coloring will not be possible.

* If everything goes well and colors are assigned successfully, we will return true at the end.


