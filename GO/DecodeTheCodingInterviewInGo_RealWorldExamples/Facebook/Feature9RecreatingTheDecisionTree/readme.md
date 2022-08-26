## Description

Facebook uses a recommendation system to recommend ads to its users. This recommendation system recommends ads on the basis of the results obtained from this decision tree. Facebook wants to implement this recommendation system for Instagram users as well. For this purpose, Facebook wants to replicate the decision tree from a Facebook server to an Instagram server.

The decision tree used in Facebook’s recommendation server is serialized in the form of its inorder and preorder traversals as strings. Using these traversals, we need to create a decision tree for Instagram’s recommendation system.

Let us say we have these preorder and inorder traversals respectively: `["subject", "viewed", "likeable", "notlikeable", "notviewed", "similar", "nonsimilar"]` and `["likeable", "viewed", "notlikeable, "subject", "similar", "notviewed", "nonsimilar" ].` The decision tree for these traversals is shown in the illustration below:

## Solution

A binary tree is a root node that comes along with its two subtrees, the left subtree and the right subtree. Each subtree is a binary tree itself.

* To find the position of the root in constant time, we will create a hashmap. This hashmap will store the value, along with its index, of our inorder traversal as key-value pairs.

* We will use pIndex, which will keep track of the element that we will use to construct the root.

* We will make recursive calls to the CreateTreeFromVal function to create the tree. This function will take a range of inorder traversal and return our binary tree. This function will:

	* Return nil if there are no elements present to construct the tree.

	* Use preorder[pIndex] to initialize the root and then increment pIndex.

	* Use the inorder traversal to recursively construct the binary tree, using the left and right positions.

* Call the CreateTreeFromVal function, using the complete range of preorder traversal.













