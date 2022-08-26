## Description

First, we need to figure out a way to traverse the DOM structure that we obtain from a single web page. The HTML can be represented in a tree structure where the children of the HTML tag become the children of a node in the tree. Each level of the tree can have any number of nodes depending upon the number of nested HTML tags. We need to traverse the nodes in the tree level by level, starting at the root node.

We’ll be provided with a root node of an n-ary tree. The root node in our case will be the body tag. This root node will have the complete web page nested within its children. We have to return the values of each levels’ nodes from left to right in separate subarrays. This way we can separately analyze their content for further data processing.

## Solution

Since we need to traverse all the nodes of each level before moving onto the next level, we can use the Breadth First Search (BFS) technique to solve this problem. We can use a queue to efficiently traverse in BFS fashion.

Let’s see how we might implement this functionality:

1. Start by enqueuing the root node to the queue.

2. Iterate until the queue is empty.

3. During each iteration, first count the elements in the queue (let’s call it queueSize). We will have this many nodes in the current level.

4. Next, remove queueSize nodes from the queue and enqueue their value in a list to represent the current level.

5. After removing each node from the queue, insert all of its children into the queue. If the queue is not empty, repeat from step 3 for the next level.




