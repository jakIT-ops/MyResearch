## Description

A city cannot be represented by a single straight road because there are numerous intersections and crossings running throughout it. In our city, there are forks in the road, making binary-tree representation possible. The furthest checkpoints of the city are leaf nodes in this binary tree; these represent the Uber service area’s limits. We want the new drivers to have a fantastic first day to kick start their career at Uber. Therefore, we want to recommend these drivers a route that would maximize the possibility of finding customers. This route should be the longest possible route so that they are bound to find a customer eventually.

## Solution

As seen in the above example, the longest path is one in which there is a maximum number of edges between two nodes or checkpoints. The edges here represent the roads. As the city structure represents a binary tree, the longest path in the tree will either pass through the root node or not. Let’s explore both of these conditions.

The longest path that passes through the root of the tree:

We can use the height of the tree when the root node is included in the longest path. The height of a tree is the longest path from the root node to any leaf node in the tree. So, the height of a tree can be considered the longest path starting from the root. We can calculate the longest path of the complete tree as:

height(root -> left) + height(root -> right) + 1(root node itself)

The path passes through the root (the +1 at the end of the above expression). It includes the deepest node in the left subtree (accounted by the first term) and the deepest node in the right subtree (the second term).


