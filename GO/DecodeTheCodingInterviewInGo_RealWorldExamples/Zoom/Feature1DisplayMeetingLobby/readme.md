## Description

For the first feature of the Zoom application, we need to develop a display structure for the list of participants attending a Zoom meeting. As you know, the names of attendees in a Zoom meeting are displayed in alphabetical order. However, attendees can join or leave a meeting at random, so the order has to be updated continuously. To tackle this issue, Zoom has decided to store the names of attendees in a binary search tree (BST). Additionally, we are specifically working on a meeting’s “Gallery Mode” display., where the participants’ names/videos are paginated (divided into pages that can be scrolled). In this scenario, we will assume that only ten participants can be shown on one page.

## Solution

We can implement this feature with the help of the in-order traversal algorithm. We will simulate an in-order traversal using a custom stack and an iterative, rather than recursive, approach. In the solution below, some helper functions are also implemented to make it modular and reusable. Let’s take a close look at the implementation of each function in the DisplayLobby type.

* `new():` This function will take the root of the BST as input and create a stack. The values of the tree will populate the stack by calling the helper function PushAll() with the root of BST as a parameter.

* `PushAll():` This function will take a node as input. We will start traversing the tree from the node provided. The value of the current node will be pushed inside the stack, and we will jump to the left child of the current node and continue the process until the current node becomes None. This way, we will be adding the leftmost branch of the tree (rooted at the input node) into the stack. For the input node, the next smallest element in the tree will always be the leftmost element in the tree. So, for a given root node, we will follow the leftmost branch until we reach a node that doesn’t have a left child. This node will be the next smallest element.

* `NextName():` This function returns the next element in stack at any moment. The stack is popped to find the next smallest element. Then, it is populated again by calling the PushAll() function on the popped element’s right child, and the popped element is returned. We do this because the function returns the smallest element of the BST. Finally, it simulates recursion by moving one step forward towards the next smallest element, which is inside the right subtree of the smallest element.

* `HasNext():` This function lets us know if the next element exists in the stack. This is done by checking if the stack is empty or not. We use this helper function to avoid exceptions.

* `NextPage():` This is the function that implements pagination by returning a maximum of ten participants at a time. Inside this function, we will call the NextName() function ten times and populate the resulting array. Before calling the NextName() function, we will call the HasNext() function to check if the stack is empty. If the stack is empty, we will break the loop and return the result.



