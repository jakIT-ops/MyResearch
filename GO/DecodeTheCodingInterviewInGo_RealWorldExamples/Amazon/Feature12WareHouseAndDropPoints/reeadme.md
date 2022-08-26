## Description

We have mapped an Amazon warehouse into a rectangular grid. There are several shelves on the floor. Furthermore, there are drop points that connect the warehouse to the delivery vans. We have robots that are programmed to fetch items from the shelves and drop them off at the nearest drop point.

The warehouse is represented as a 2D array. A cell with -1 represents a shelf, a cell with 0 represents a drop point, and the infinite value represents an open space (corridor) that the robot can tread to move from shelves to the nearest drop points.

Robots need to navigate the warehouse to pick up items, one at a time, and drop them off at the nearest drop points. The distances from every open space to the nearest drop point need to be pre-computed for efficiency.

An open space in a warehouse is represented by an infinite value. In this case, we will consider 2^{31} - 1 = 2147483647
2 
31
 −1=2147483647
 an infinite value. The distance from any open space to the nearest drop point will not exceed this value.

Our task is to precompute the distance between every cell and its nearest drop point, so that the robots can use these precomputed distances to decide on the shortest routes.

## Solution

Let’s approach this problem in the following way:

* Instead of searching for the drop point from an open space, we can search for each open space from each drop point at the same time.

* To implement this, we will use breadth-first search (BFS).

	* We will initiate BFS from all the drop points at the same time.

	* Since BFS touches all the blocks at a distance d before those at a distance d + 1, we are guaranteed to find the shortest distance to each open space.

	* We can use a queue to implement the BFS.




