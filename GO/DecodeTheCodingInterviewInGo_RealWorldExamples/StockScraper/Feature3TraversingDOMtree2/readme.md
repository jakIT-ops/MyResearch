## Description

The technique we used previously to traverse through the web tree used too much space. The number of web pages can be enormous, and traversing all of them will consume a lot of unnecessary space. Therefore, we have come up with a better approach in which we create a shadow tree for the DOM where each node has a pointer to the next node to its right on the same level. We’ll introduce an additional attribute, next, to our TreeNode structure. The next node will point to its immediate right node on the same level. If there is no right node to point, next will point to null. This next pointer will allow us to avoid the queue data structure that we used previously to traverse the tree, resulting in a space-efficient approach.

We’ll be provided with a root node of an n-ary tree. The root node in our case will again be the body tag. This root node will have the complete web page nested within its children. We have to go through each node and assign the next pointer to the node to its immediate right on the same level.

## Solution

The tree structure that we get from the web is arbitrary, meaning a parent node can have any number of child nodes and the probability of a perfect tree is very low. So, we have no idea about the structure of the tree or its branches, and we want efficient access to all nodes that are on the same level.

If we are on a node N at a level L, we have access to all of its children on level L + 1. This is the perfect time to establish the children’s next pointers. If we decide to establish the next pointers after getting on level L + 1, there will be issues connecting the children of different parents. Therefore, we’ll only move down a level from a parent node when all of the children nodes have their next pointers established.

Let’s see how we might implement this functionality:

1. We will start our traversal from the root node. There is only one node at the first level whose next automatically points to null. So, we’ll not yet move to the next level but will first establish the next pointers of the children of the root node.

2. We now need to find the next level’s leftmost node to be the starting point for assigning the next pointers. The four candidate leftmost nodes for our varying tree structures are shown in the illustration to the right. After assigning the next pointers of each node for a level, the leftmost node will need to be updated for the next level.

3. We’ll also maintain a curr pointer that will be used to traverse current level’s nodes. Since the next pointers of the current level L were established on level L - 1, we can simply traverse these nodes like a linked list. For each curr node we traverse, we’ll update its children’s next pointers.

4. Now, we’ll use a prev pointer to establish the next pointers using the curr pointer. Initially, we’ll make it equal to the next level’s leftmost node. When the curr is updated, we assign prev.next to the first child of the curr if it exists. After this, the prev pointer is also updated to the same node, so the correct next pointer is assigned in the subsequent iterations.




