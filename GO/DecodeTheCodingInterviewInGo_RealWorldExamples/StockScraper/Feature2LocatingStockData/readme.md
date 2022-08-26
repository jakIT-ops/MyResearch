## Description

Now, we need to identify which nodes of the website’s DOM tree contain the stock data. The data we are looking for is the dates on which a certain stock price went up or down. Identifying stock data in arbitrary HTML can be hard, so we’ll use the following technique.

Like the previous lesson we’ll traverse the DOM tree, assigning a score to nodes on how likely they are to be a date or a stock percentage based on the text inside of them. To make the process efficient, we also want to limit the DOM subtree that we are processing.

Here’s the scoring criteria for how likely a node is a date:

* A node whose text starts with a capital letter

* A node whose text ends in a number

* A node whose text contains the # symbol

* A node whose text is under ten characters

Here’s the scoring criteria for how likely a node is a stock percentage:

* A node whose text is short

* A node whose text contains a number

* A node whose text contains the + or - sign

* A node whose text contains the % sign

After this step, we’ll find two nodes: one node with a high date score and one with a high stock percentage score. We’ll calculate the LCA(Lowest Common Ancestor) of these two nodes. In most cases, the subtree of the LCA node will have all the dates and their respective stock percentages. This saves us time for searching the rest of the DOM tree.i


## Solution

Let’s say that our two identified nodes are a and b.

We can save the parent nodes of each node while traversing the tree. Then, we can store the parents of one of the nodes, say a, into a set. As we go from the node b towards the root, the first ancestor of b that we find in the set is the LCA. We can store the parent pointers in a dictionary for retrieval in constant time. For backtracking, we can use the set data structure.

Let’s see how we might implement this functionality:

1. First, we’ll traverse the tree starting from the root node.

2. Then, we’ll store the parent of each node in the dictionary until the nodes a and b are not found.

3. If the nodes a and b are found:

	* Traverse over the parents/ancestors of node a.

	* For each parent node, add it to the ancestors set.

4. Similarly, we will traverse through the ancestors of node b. If the ancestor is present in the ancestors set for a, this is the first ancestor common in between a and b (while traversing upwards), and this is the LCA node.
