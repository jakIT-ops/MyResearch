## Description

In this feature of the Amazon website, we want to implement a search filter that searches for products in a given price range. The product data is given to us in the form of a binary search tree, where the values are the prices. You will be given the parameters low and high; these represent the price range the user selected. This range is inclusive.

## Solution

We can implement this feature by using a variation of the preorder traversal on the binary tree. Other binary tree traversals can also be used. The complete algorithm is given below:

1. We will use a recursive helper function for the preorder traversal.

2. In this function, we will first check if the value at the current node is in the given range or not. If the value is in range, we will add it to the output array.

3. Then, we will recursively call the preOrder function on the left child of the node, but only if the value of the current node is greater than or equal to low. This way we will minimize the traversal.

4. Similarly, if the value of the current node is less than or equal to high, we will also recursively traverse the right child of the node.

5. The output will be returned when the traversal is done.

